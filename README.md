# Ghost Labs

Marketing site for **Ghost Labs, LLC** — a boutique software studio — and its first app, **Tidy Task & Loot**.

Live site: https://lunchbox-1010.github.io/ghost-labs.github.io/

## What's here

```
.
├── index.html                    Homepage (hero, projects, about, contact)
├── README.md                     This file
├── assets/
│   ├── logo.png                  Brand logo (color)
│   ├── styles.css                Shared stylesheet
│   └── app.js                    Mobile menu + footer year
└── tidy-task-and-loot/
    ├── index.html                App overview & feature pages
    ├── privacy.html              Privacy Policy (App Store / Google Play ready)
    ├── terms.html                Terms of Service / EULA
    └── support.html              FAQ + support contact
```

## Tech

Plain static HTML, CSS, and a tiny vanilla JS file. No build step, no framework, no dependencies. Open `index.html` in any browser to preview locally.

## Brand

| | |
|--|--|
| Orange | `#E97B2A` |
| Blue   | `#3B7FB0` |
| Ink    | `#0E1116` |
| Soft   | `#F6F7F9` |
| Text   | `#1F2937` |

Brand variables live at the top of `assets/styles.css` if you ever need to tweak them.

## Deploy

This repo is hosted on **GitHub Pages**.

1. Repo Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main`, folder `/ (root)`
4. Save — site rebuilds automatically on every push.

## Updating

Edit any HTML file directly in the GitHub web editor (pencil icon → edit → commit) and the site rebuilds in about a minute.

To swap the logo, replace `assets/logo.png` with a new file of the same name. All five HTML files reference it from there.

## Adding a new app

1. Duplicate the `tidy-task-and-loot/` folder and rename it (e.g. `next-app/`).
2. Update the page titles, copy, and crumbs in each of the four HTML files.
3. On `index.html`, add a new project card in the `#projects` section pointing at `next-app/index.html`.
4. Commit and push.

## Contact

contact@ghost-labs.com

## License

© Ghost Labs, LLC. All rights reserved.
