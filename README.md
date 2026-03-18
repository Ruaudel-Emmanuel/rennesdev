Developer Portfolio – Next.js
A minimal personal website built with Next.js (App Router) to present my freelance developer activity, display my daily rate, and collect leads through a Tally contact form.

Features
Single-page layout with:

Short introduction and services

Display of current daily rate (TJM)

Contact section powered by a Tally form embed

Built with the Next.js App Router

Simple responsive layout using basic CSS

Ready to be deployed on any Node.js hosting provider (including Infomaniak)

Tech Stack
Next.js 14 (App Router)

React 18

TypeScript or JavaScript (choose when creating the app)

Tally for the contact form embed

Getting Started
1. Install dependencies
bash
npm install
# or
yarn install
# or
pnpm install
2. Run the development server
bash
npm run dev
# or
yarn dev
# or
pnpm dev
Open your browser at http://localhost:3000 to view the site.

Project Structure
bash
app/
  layout.tsx      # Root layout and metadata
  page.tsx        # Main page (intro + rate + contact)
  globals.css     # Global styles
next.config.mjs   # Next.js configuration
package.json      # Dependencies and scripts
Tally Contact Form
The contact section uses a Tally embed inside app/page.tsx.

Replace YOUR_FORM_ID in the data-tally-src attribute with the ID of your own Tally form:

tsx
<iframe
  data-tally-src="https://tally.so/embed/YOUR_FORM_ID?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
  ...
></iframe>
You can find the form ID and embed code from your Tally dashboard under “Share” → “Embed”.

Production Build
Build the application for production:

bash
npm run build
npm run start
This will start the app in production mode on port 3000 by default.

Deployment Notes (Node.js hosting)
On a Node.js hosting platform (such as Infomaniak):

Upload the project files

Install dependencies (npm install)

Run the production build (npm run build)

Configure the start command to npm run start

Make sure the correct Node.js version is selected in your hosting environment

Customization
Update the text content (name, services, daily rate) in app/page.tsx

Adjust styles in app/globals.css and inline styles

Optionally add more sections (projects, skills, testimonials) as additional components or routes
