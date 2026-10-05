# Ghost Labs website

The marketing site for Ghost Labs, LLC at https://ghost-labs.com: plain static HTML, CSS and a small vanilla JS file, served by GitHub Pages from `main` at the root. There's no build step. Pushing to `main` publishes within about a minute. README.md has the brand colors and the page map.

## Where things live

| Path | What |
|---|---|
| `index.html` | Homepage (hero, the three foundries, product spotlight, about, contact) |
| `apps/`, `enterprise/`, `foundry/` | App Foundry, Enterprise Foundry, Brand Foundry; `cloud/` redirects to `enterprise/` |
| `maven-babelfish/` | Product pages and its brand kit (the swimming fish: `.fish-icon` at the end of `assets/styles.css`; the pivots are measured, don't change them) |
| `tidy-task-and-loot/` | App pages, privacy, terms, support (store-ready) |
| `babelfish/`, `licence/` | Download and licence pages published by the Maven BabelFish release tooling ("licence: publish what changed" commits) |
| `assets/styles.css` | Shared styles; brand variables at the top |

## Working on it

- Preview: open `index.html` in a browser, or `python3 -m http.server` in the repo root.
- New app: copy `tidy-task-and-loot/`, update its four pages, and add a card to `apps/index.html`. New enterprise product: a card in `enterprise/index.html` plus its own directory, with `chip-dev` until it ships.
- Publishing is a push to `main`, which is Larry's step.

## Never

- Anything not meant to be public. Pages serves every folder not starting with `_`, so a private file beside a page is published. Client work goes in a private repo.
- Larry's personal details. The site carries Ghost Labs, LLC's contact (contact@ghost-labs.com).

## Sessions and the board

- The board of record is Ravenwood (https://ravenwood.ghost-labs.com), through the Ravenwood connector. Project key: **GL**.
- Before the first edit, find the item (`list_items` with `project: "GL"` and `text`) or create it, and put it In progress. Add notes as steps land.
- Check in on the item you work: `Session started: Ghost Labs business and website, <surface>, <link>`. When you stop: `Session parked: <where it stopped>. Next: <the resume line>`. When it's done: `Session finished`.
- "Pick up GL-123" means: read that item's latest `Session parked` note and carry on from it.
- Larry's own steps (a build, an install, a deploy, a push, a portal change, a decision) go on the Development board's Checklist, linked to the item, with exact commands and full paths.
- Keep context lean: read the board filtered by project, `/clear` between tasks, and use subagents for big surveys.
- Standing rules: a new visible version on every build; a passing security scan of exactly that code before anything is signed, notarized or uploaded; all documentation in US English.
