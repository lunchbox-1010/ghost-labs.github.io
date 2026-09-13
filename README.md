# Ghost Labs

Marketing site for **Ghost Labs, LLC** — a boutique software studio organised as three foundries.

Live site: https://ghost-labs.com

| Foundry | Directory | What it is |
|---|---|---|
| **App Foundry** | `apps/` | Consumer apps. Currently **Tidy Task & Loot**. |
| **Enterprise Foundry** | `enterprise/` | Business software and the Azure platforms it runs on — architecture, security, AI — plus our own products. First product: **Maven Babelfish**. |
| **Brand Foundry** | `foundry/` | Web and brand design. |

`cloud/` is a redirect stub: the cloud practice became Enterprise Foundry, and old links still land there.

## What's here

```
.
├── index.html                    Homepage (hero, the three foundries, about, contact)
├── apps/index.html               App Foundry
├── enterprise/index.html         Enterprise Foundry (services + products)
├── foundry/index.html            Brand Foundry
├── cloud/index.html              Redirect stub -> enterprise/
├── README.md                     This file
├── assets/
│   ├── logo.png                  Brand logo (color)
│   ├── styles.css                Shared stylesheet
│   └── app.js                    Mobile menu + footer year
├── maven-babelfish/              Product page + its own brand kit
│   ├── index.html                The name page: two definitions that turn into the pitch
│   ├── fish/                     The swimmer, cut into tail and body layers, five colours
│   ├── scene/                    The mark pulled apart — corner art, and the disc minus the fish
│   └── brand/                    Maven Babelfish logo at every size
└── tidy-task-and-loot/
    ├── index.html                App overview & feature pages
    ├── privacy.html              Privacy Policy (App Store / Google Play ready)
    ├── terms.html                Terms of Service / EULA
    └── support.html              FAQ + support contact
```

### The Maven Babelfish mark, animated

`assets/styles.css` ends with a `.fish-icon` component. The brand kit ships the disc with the
fish lifted out of it, so the two fish layers drop back on top at `inset:0` and reconstruct the
logo exactly — then the tail and body counter-rotate about their measured pivots (`38.3% 50.1%`
and `66.4% 49.8%`) and it swims. Those origins are measured, not guessed; changing them makes the
fish look like it is being waved about on a stick. Drop it in with:

```html
<span class="fish-icon" aria-hidden="true">
  <span class="swim"><i class="tail"></i><i class="body"></i></span>
</span>
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
3. On `apps/index.html`, add a new project card in the `#projects` section pointing at `../next-app/index.html`.
4. Commit and push.

## Adding a new enterprise product

Add a card to the `#products` section of `enterprise/index.html` and give the product its own
directory at the repo root. Use `<span class="chip-dev">In development</span>` beside the heading
until it ships, and take it out when it does.

## Contact

contact@ghost-labs.com

## License

© Ghost Labs, LLC. All rights reserved.
