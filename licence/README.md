# `/licence/` — one signed file per paying Maven BabelFish account

Read this before you touch anything in this folder.

**Every file in here is one paying customer's subscription. Removing a file takes a customer's
subscription away. Nothing in this folder looks important and every file in it is.**

There is no index page here and there must never be one, so this README is the only warning
anybody gets.

## What is in here

One file per account, named `<key>.json`, where the key is a long string of hexadecimal characters
that means nothing at all. Inside each file: that same key, the day it was issued, the day it runs
out, two numbers of days, a layout number, and a signature Ghost Labs made with a key that is not in
this repository and never will be.

That is the whole of it. There is no company name, no person, no email address, no domain, no seat
count, no price, no invoice number and no customer data of any kind, in the file or in its name.
**Which key belongs to which customer is written down in Ghost Labs' own records and nowhere else.**

This folder is public. Anybody who guesses an address can fetch the file at it, because that is what
a static website does. What they learn from a file is that some account exists and runs until some
date, which is nothing. What they would learn from a file named after a company is that that company
is a Ghost Labs customer, for the length of their subscription, for ever after in the repository's
history. That is why the names mean nothing.

## What removing a file does

A customer's copy of Maven BabelFish fetches its own file from this folder every couple of weeks. If
the file is not there, the fetch fails, and BabelFish carries on with the licence it last collected
until that licence genuinely runs out. Then, after the grace period written inside the licence, two
things stop on that customer's machine:

- **no new data is collected** — no marketing platform is read, nothing new arrives;
- **their own AI is no longer answered.**

Three things never stop, in any state, for any reason: reading the figures that account already
holds, exporting them, and every other way of getting their own data out. Their marketing data is
theirs, it lives on their own machines, and nothing here can reach in and take it.

**So do not tidy this folder.** A subscription that has ended is ended by not renewing it, and the
file expires on its own. An account whose file is deleted by somebody clearing out old-looking
things is an account that stops working weeks later for a reason nobody will connect to the deletion.

## What breaks if these files move

The address a customer's install asks for is compiled into that install. It cannot be changed
afterwards — not by us, not by them, not by a redirect. It is:

    https://ghost-labs.com/licence/<key>.json

Rename this folder, move it under `/maven-babelfish/`, or fold it into a redesign, and every paying
customer's BabelFish starts asking for a page that is not there. Rename one file and that one
customer does. **A renewal is a new file written over the old one at the same address**, never a new
name: a new name leaves that customer on a file nobody will ever update again, and the only way back
is an engineer editing a configuration file on their computer.

## What must never go in here

- **No index page, and nothing that lists what is in here.** GitHub Pages does not list a directory
  that has no index, so the safe thing is to add none. A list of these files is a count of Ghost
  Labs' customers and a timeline of when each of them signed.
- **Nothing that says which key belongs to whom.** Not a file, not a line in this README, not a
  comment, and **not a commit message** — the history of a public website is public for ever, and a
  name removed in a later commit is still in the history that published it.
- **No company name, person, email address or domain**, anywhere in this folder, in any form.
- **No private key.** Licences are signed on the machine that holds the Ghost Labs signing key, which
  is on an encrypted drive and never in a repository. Only the signed result is copied here.
- **Nothing that is not a licence.** This README, and one `<key>.json` file per account. That is all.

## How a file gets here, and how it leaves

Every one of these files is written by `tools/support/ghost_labs_licences.py` in the BabelFish
repository, on the machine where the Ghost Labs signing key lives. It mints a licence for a new
account, renews one over the same file at the same address, says what is published here and whether
it has actually been pushed, and — rarely, and only after making the person running it read what it
costs — takes one back off. It pushes nothing itself.

Do not write a file in here by hand, and do not copy one in from somewhere else. The tool refuses to
create a second file for an account that already has one, which is the mistake that strands a
customer, and it checks this whole folder before it will tell anybody to publish anything.

If you have found this folder and something in it looks wrong, the safest thing you can do is
nothing. Ask Ghost Labs first. There is a support address on the Maven BabelFish product page.

## `.nojekyll`

There is a `.nojekyll` file at the root of this repository and it matters to this folder. Without it
GitHub Pages runs a Jekyll build over everything before serving it, and one of the things that build
does is turn a `README.md` in a folder with no index into the page served at that folder's address —
which would publish this warning as `https://ghost-labs.com/licence/`, an index page in the one
folder that must not have one. It also means what is committed is what is served, byte for byte,
which is what a signature check needs.
