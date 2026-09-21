# `/babelfish/` — the files Maven Babelfish fetches about its own builds

Nobody browses this folder. Two files live here and both are read by software, on a schedule, from
addresses that are compiled into every copy of Maven Babelfish that has ever been installed.

| File | Who reads it | What it is |
|---|---|---|
| `appcast.xml` | The Mac application, once a day | The Sparkle update feed. It says which versions exist, where the archive is, and carries a signature over each one |
| `releases.json` | The machine that holds a customer's account, every couple of weeks | The signed file naming the published version of each of the four reading applications. It is how somebody running an old copy finds out a new one exists |

The product pages that a person reads are at `/maven-babelfish/`, and one signed file per paying
account is at `/licence/`. Three folders, on purpose, and the next section is why.

## What breaks if these files move

**Everything, quietly, and there is no way back.** An address a machine fetches is built into every
copy that has ever shipped. An install only ever knows the address it was born with, so renaming
this folder, moving it under `/maven-babelfish/`, or folding it into a redesign does not redirect
anybody — it makes every installed copy in the world start asking for a page that is not there.

- Move or delete `appcast.xml` and every Mac silently stops receiving updates. Nothing appears
  broken. Nobody notices for a year.
- Move or delete `releases.json` and every customer goes on being told about whatever version their
  own machine last heard of, for ever.

That is the whole reason this folder is not under `/maven-babelfish/`. A product page exists to be
rewritten — that is what a product page is for. This folder exists to never move.

The addresses, written out once, are:

    https://ghost-labs.com/babelfish/appcast.xml
    https://ghost-labs.com/babelfish/releases.json

In the Babelfish repository every one of them is built from a single named constant in
`engine/src/babelfish/addresses.py`, and a check fails if the same address is ever typed out a
second time anywhere else.

## What must never go in here

- **Nothing a person is meant to read.** No `index.html`, no landing page, no download button. The
  page with the download button on it belongs at `/maven-babelfish/`, where somebody can redesign it
  without touching anything a machine asks for.
- **Nothing about a customer.** Licences are in `/licence/`, and the two folders are kept apart so
  that a person or a script tidying up build files can never touch a paying customer's entitlement.
  Deleting a file in here costs a re-upload. Deleting one in there stops somebody working.
- **No private key, ever.** Both files are signed somewhere else, on the machine that holds the
  signing keys. Only the signed result is copied here.
- **Nothing served over plain http.** Every address in and about these files is https. A file that
  decides what a customer's computer downloads and installs must not be one that anybody on the same
  network can answer.

## How each file gets here

`appcast.xml` is written by `apps/macos/release/publish.sh` in the Babelfish repository, which merges
each new release into whatever is already published. **Old entries are kept**, so an install two
versions behind still finds a path forward. Do not hand-edit it once it is live: copy the file
`publish.sh` produces over this one and push.

`releases.json` is minted by `tools/support/ghost_labs_support.py releases`, on the machine where the
Ghost Labs signing key lives. Copy what it writes over this one and push.

**The `releases.json` in here today is a placeholder.** It names no release and carries no signature,
which is honest: nothing has been published to a customer yet. It is here so that the address is
live and correct while nothing depends on it. It must be replaced with a real, signed one before
`releases_public` is ever pinned into a shipped build, because pinning that key is the moment every
installed copy starts fetching this address. The file says so in its own text.

## `.nojekyll`

There is a `.nojekyll` file at the root of this repository and it matters to this folder. Without it
GitHub Pages runs a Jekyll build over everything here before serving it, which would rewrite the
`README.md` in this folder into a page and does not guarantee that what is committed is what is
served. Both files in here are checked byte for byte against a signature. A file altered on its way
to the web is a file every customer's copy of Babelfish refuses, on the same afternoon, with a
message that sounds like the customer's fault.
