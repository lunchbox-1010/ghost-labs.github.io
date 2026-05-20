#!/usr/bin/env python3
"""
Encrypt source/index.html into a password-gated page.

Format (all hex strings):
  - salt: 16 bytes
  - iv:   16 bytes
  - ct:   AES-256-CBC ciphertext (PKCS7 padded)
  - mac:  HMAC-SHA256 over (salt || iv || ct), using HMAC key

Key derivation:
  PBKDF2-HMAC-SHA256, 200,000 iterations, 64 bytes output.
    bytes[0:32]  = AES-256 key
    bytes[32:64] = HMAC key
"""
import os, sys, json, hmac, hashlib, base64, pathlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITER = 200_000
KEY_LEN = 64

def derive(password: str, salt: bytes) -> tuple[bytes, bytes]:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=KEY_LEN, salt=salt, iterations=ITER)
    k = kdf.derive(password.encode("utf-8"))
    return k[:32], k[32:]

def encrypt(plaintext: bytes, password: str) -> dict:
    salt = os.urandom(16)
    iv   = os.urandom(16)
    aes_key, mac_key = derive(password, salt)
    padder = PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    enc = cipher.encryptor()
    ct = enc.update(padded) + enc.finalize()
    mac = hmac.new(mac_key, salt + iv + ct, hashlib.sha256).digest()
    return {
        "salt": salt.hex(),
        "iv":   iv.hex(),
        "ct":   ct.hex(),
        "mac":  mac.hex(),
        "iter": ITER,
    }

def main():
    here = pathlib.Path(__file__).parent
    src = (here / "index.html").read_text(encoding="utf-8")
    password = os.environ.get("CG_PASSWORD", "granite2026").strip()
    payload = encrypt(src.encode("utf-8"), password)

    # The unlock page (lightweight: only the gate UI + decryption JS).
    gate = (here / "gate_template.html").read_text(encoding="utf-8")
    out = gate.replace("__PAYLOAD__", json.dumps(payload))
    (here.parent / "index.html").write_text(out, encoding="utf-8")

    print(f"Encrypted with password: {password!r}")
    print(f"Wrote: {here.parent / 'index.html'}  ({len(out):,} bytes)")
    print(f"PBKDF2 iterations: {ITER:,}")

if __name__ == "__main__":
    main()
