import './globals.css';
import type { ReactNode } from 'react';

export const metadata = {
  title: 'Emmanuel – Développeur Python / Automation',
  description: 'Freelance Python, n8n, automatisation et développement web.'
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
