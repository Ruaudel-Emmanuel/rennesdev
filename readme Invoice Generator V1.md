# Structured Invoice Generator V1

A lightweight client-side HTML prototype for `rennesdev.fr` that collects key French invoice fields, renders a readable invoice preview, generates a downloadable PDF, and exports structured XML for future e-invoicing work.[web:165][web:185]

## Purpose

This V1 is a fast, free website component intended to demonstrate the concept, test user interest, and provide immediate utility on the public site before a more advanced VPS-backed version is developed.[web:183][web:189]

It is designed as a **transition tool** toward French e-invoicing, not as a complete certified compliance engine.[web:165][web:166]

## What the prototype does

- Collects seller, buyer, invoice, and line-item information required for a standard French invoice.[web:185][web:188][web:190]
- Includes key reform-related fields such as customer SIREN, delivery address, transaction nature, and the “VAT on debits” mention when applicable.[web:182][web:188]
- Displays a live invoice preview in the browser.
- Generates a readable PDF directly in the browser.
- Exports a separate structured XML file inspired by future e-invoicing data flows.[web:165][web:176]
- Works as a static HTML page with no server dependency for V1.

## What the prototype does **not** do

This V1 does **not** generate a fully compliant Factur-X invoice.[web:165][web:166][web:170]

A true Factur-X file is a hybrid electronic invoice format that combines:
- a human-readable PDF/A-3 document, and
- embedded XML structured according to the accepted standard.[web:165][web:166][web:176]

In this prototype, the PDF and the XML are generated separately. That makes the page useful for demonstration, data capture, and early testing, but not sufficient for full regulatory compliance.[web:165][web:176][web:180]

## Why this approach makes sense for V1

The French 2026–2027 e-invoicing reform is centered on structured invoice data and accepted formats such as Factur-X, UBL, and CII.[web:165][web:166][web:180] For a solo developer shipping a first public version quickly, a static browser-based prototype is a practical way to validate the use case without taking on the technical complexity of PDF/A-3 generation, XML embedding, storage, account management, or platform integrations too early.[web:183][web:189]

## Main invoice fields covered

The prototype is built around the practical data expected on French invoices, including:[web:185][web:188][web:190]

- Seller legal name
- Seller SIREN and SIRET
- Seller VAT number
- Seller address
- Buyer legal name
- Buyer address
- Buyer SIREN
- Buyer VAT number
- Delivery address
- Invoice number
- Invoice issue date
- Due date
- Payment terms
- Transaction nature
- VAT on debits option
- Line descriptions, quantities, unit prices, VAT rates, totals

## Technical overview

The page is intentionally simple:

- **Single static HTML file** for easy integration into `rennesdev.fr`
- **Client-side JavaScript** for calculations, preview rendering, PDF generation, and XML export
- **No database**
- **No backend**
- **No authentication**
- **No persistent storage**

This makes deployment easy and keeps hosting costs close to zero for the first release.

## Intended use cases

V1 is suitable for:

- Demonstrating the concept on a portfolio or freelance website
- Collecting early feedback from small business owners
- Showing a working prototype on mobile during conversations or meetings
- Testing whether users value invoice generation plus structured export
- Preparing the roadmap for a more serious VPS-based version

## Recommended positioning on the website

Suggested positioning for this V1:

> Free structured invoice generator for early testing and transition toward French e-invoicing.

Recommended wording to avoid overpromising:

- “Prototype”
- “V1”
- “Free tool”
- “Prepares the transition toward e-invoicing”
- “PDF + structured XML export”

Wording to avoid at this stage:

- “Certified Factur-X generator”
- “Fully compliant e-invoicing solution”
- “Official reform-compliant platform”

## Limitations

Known limitations of this V1:

- No embedded XML inside PDF/A-3, so not true Factur-X.[web:165][web:166]
- No server-side validation.
- No numbering controls.
- No archival workflow.
- No platform integration.
- No digital signature.
- No tax or accounting system integration.
- No user account system.

## Next version ideas

A more professional VPS-based version could add:

- secure storage of invoices and XML files
- account management
- server-side PDF generation
- better validation rules
- invoice numbering logic
- customer database
- legal archiving workflow
- true Factur-X generation with embedded XML in PDF/A-3
- future interoperability with e-invoicing platforms or partner services[web:165][web:166][web:183]

## Summary

This V1 is a lean public-facing prototype: useful, fast to deploy, easy to demonstrate, and realistic for a solo freelancer. It is best understood as a practical first step toward a more advanced e-invoicing product, not as the final compliant solution.[web:176][web:189]
