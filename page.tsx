'use client';

import Script from 'next/script';

export default function HomePage() {
  return (
    <main
      style={{
        minHeight: '100vh',
        maxWidth: 800,
        margin: '0 auto',
        padding: '3rem 1.5rem',
        fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, sans-serif'
      }}
    >
      <header style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.4rem', marginBottom: '0.5rem' }}>
          Emmanuel – Développeur Python & Automation
        </h1>
        <p style={{ fontSize: '1.1rem', color: '#555' }}>
          Freelance · Python, Django, n8n, intégration d’API, automatisation de processus métier.
        </p>
      </header>

      <section style={{ marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.6rem', marginBottom: '0.5rem' }}>Ce que je fais</h2>
        <p style={{ lineHeight: 1.6 }}>
          Je conçois des scripts et applications sur mesure pour automatiser vos tâches répétitives,
          connecter vos outils (CRM, ERP, SaaS) et fiabiliser vos flux de données.
        </p>
      </section>

      <section style={{ marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.6rem', marginBottom: '0.5rem' }}>TJM & modalités</h2>
        <p style={{ lineHeight: 1.6 }}>
          TJM indicatif&nbsp;: <strong>XXX&nbsp;€ HT</strong>.  
          Interventions à distance, démarrage possible sous 7 jours, facturation via Malt ou en direct.
        </p>
      </section>

      <section id="contact">
        <h2 style={{ fontSize: '1.6rem', marginBottom: '0.5rem' }}>Me contacter</h2>
        <p style={{ lineHeight: 1.6, marginBottom: '1rem' }}>
          Décrivez brièvement votre besoin&nbsp;: je reviens vers vous sous 24&nbsp;h ouvrées.
        </p>

        {/* Tally embed */}
        <iframe
          data-tally-src="https://tally.so/embed/YOUR_FORM_ID?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
          loading="lazy"
          width="100%"
          height="320"
          frameBorder={0}
          marginHeight={0}
          marginWidth={0}
          title="Formulaire de contact"
        ></iframe>

        <Script
          id="tally-js"
          src="https://tally.so/widgets/embed.js"
          onLoad={() => {
            // @ts-ignore
            if (typeof Tally !== 'undefined') {
              // @ts-ignore
              Tally.loadEmbeds();
            }
          }}
        />
      </section>
    </main>
  );
}
