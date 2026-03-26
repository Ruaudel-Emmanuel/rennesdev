
# rennesdev.fr – Freelance Automation Website

This project is the marketing website for my freelance activity as a Python & automation.  
It is a **single-page PHP/HTML site** hosted on Infomaniak, designed to be fast, simple to maintain, and focused on lead generation.

## Why I pivoted from Node/Next.js to PHP

Initially, I started with a Next.js (Node.js) stack to host the site on Infomaniak.  
While this works technically, it quickly introduced unnecessary complexity for a simple one-page website:

- Build and runtime management: I had to handle `npm install`, `npm run build`, and `npm run start` on a constrained shared hosting environment.  
- Limited SSH resources: builds often got stuck at “Collecting page data”, requiring the use of Infomaniak’s Node.js Builder to complete.  
- Overkill for the need: the site is basically static content plus a Tally contact form, so the benefits of React/Next.js were minimal compared to the operational overhead.

Because the **business goal** is to have a clear, reliable landing page that converts visitors into leads, I decided to pivot to a classic PHP/HTML stack:

- No build step, no Node.js runtime to manage.  
- Deployment is just “upload files via FTP/WebFTP”.  
- Easier to maintain over time while I focus on client work, not infrastructure.

## Simple project structure

The site lives at the root of the Infomaniak web hosting:

```text
rennesdev.fr/
  index.php              # Single-page site
  assets/
    css/
      style.css          # Global styles
    img/
      banniere-codeur.jpg  # Banner visual
```

- `index.php` contains all the content sections: hero, services, pricing packages, about, and contact.  
- `style.css` provides a minimal, responsive layout that reflects the banner’s dark/tech visual identity.  
- The banner image is used as a background in the hero section.

## Content and positioning

The page is designed around a clear positioning:

- **“Automatisation IA & API Python”** for SMEs and independents.  
- Promise: helping clients save around **10 hours per week** on repetitive tasks.  
- Social proof and credibility are supported by links to my LinkedIn, Malt profile, and technical portfolio.

Main sections:

1. **Hero**  
   - Headline: automated, custom solutions, aligned with my LinkedIn messaging.  
   - Short subtitle explaining what I do and who I help.  
   - Primary CTA: “Parler de votre projet” linking to the contact section.

2. **What I do**  
   - Description of automation work: workflows, API integrations, dashboards.  
   - Three pillars: business automation, APIs & integrations, dashboards.

3. **Packages (forfaits)**  
   - “Forfait Automatisation PME” – around 2,000 € for a two-week engagement (analysis, 1–2 workflows, simple dashboard, training).  
   - “Forfait Indépendants & Freelances” – a lighter package focused on admin/workflow automation.  
   - “Forfait Site Internet” – a website package (1,000–1,500 €) including a simple site and an integrated contact form.

4. **About**  
   - Short bio: mix of project management, field experience, and automation expertise.  
   - Links to LinkedIn, Malt, portfolio.

5. **Contact (Tally form)**  
   - A Tally form embedded via an `<iframe>`, connected to my Notion workspace.  
   - The goal is to collect qualified leads with a brief description of their pain points and automation needs.

## How it will be deployed

Deployment is intentionally simple:

1. Edit and test `index.php` and `assets/css/style.css` locally in a browser.  
2. Upload the files to the Infomaniak PHP web hosting via FTP/WebFTP.  
3. Replace `YOUR_FORM_ID` in the Tally embed URL with the actual Tally form ID.  
4. Verify that `https://rennesdev.fr` serves the single-page site and that the Tally form submits data correctly to Notion.

This approach keeps the stack as lightweight as possible so I can spend time on **client-facing automation projects** instead of debugging Node.js builds on shared hosting.
