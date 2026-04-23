# RennesDev Website

Official static website for RennesDev, the freelance business of Emmanuel Ruaudel.

This project is a lightweight HTML/CSS website focused on:
- clear positioning for SMEs and independent professionals,
- better technical SEO foundations,
- simple maintenance and deployment,
- compatibility with standard static hosting environments such as Infomaniak.

## Project Goal

The website promotes freelance services around:
- python automatisation 
- API integrations,
- workflow automation,
- dashboards and operational tools,
- process optimization for small businesses.

The site is designed to stay simple, fast, readable, and easy to update without a framework.

## Current Stack

- HTML5
- CSS3
- Static assets
- Tally form integration
- Google Tag Manager
- JSON-LD structured data

No JavaScript framework, no build step, no backend required.

## File Structure

```text
rennesdev.fr/
├── index.html
├── portofolio.html
└── assets/
    ├── css/
    │   └── style.css
    └── img/
        └── banniere-codeur.jpg
```

## Important Paths

Because the site is deployed with this structure, asset paths must match it exactly.

### In `index.html`

CSS:
```html
<link rel="stylesheet" href="./assets/css/style.css">
```

Hero image:
```html
<img src="./assets/img/banniere-codeur.jpg" alt="" class="hero__bg">
```

Social preview image:
```html
<meta property="og:image" content="https://rennesdev.fr/assets/img/banniere-codeur.jpg">
<meta name="twitter:image" content="https://rennesdev.fr/assets/img/banniere-codeur.jpg">
```

## SEO Improvements Included

The current version includes:
- a unique title tag,
- a meta description,
- canonical URL,
- Open Graph tags,
- Twitter Card tags,
- structured data with `ProfessionalService`,
- semantic section structure,
- internal anchor navigation,
- service-oriented headings,
- local intent around Rennes and Brittany.

These elements support technical SEO, content clarity, and better page interpretation by search engines. [web:83][web:86]

## Navigation

The main navigation currently links to:
- Services
- Portfolio
- About
- Contact

If the portfolio page keeps the current filename, use:
```html
