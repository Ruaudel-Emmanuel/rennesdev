# Architecture globale du VPS — Rennesdev

## Vue d’ensemble

L’architecture active du VPS est maintenant clarifiée : la production principale Rennesdev tourne depuis `/home/manu/var/www/api-rennesdev-backend`, une ancienne copie de `/var/www/api-rennesdev-backend` a été archivée, `facturx-api` a été supprimé, et les services Docker encore présents sont `n8n` et `diagnostic-api`.[cite:1]

Le point important à retenir est que les ports du serveur ont maintenant un rôle bien identifié, ce qui évite les doutes pour la suite de l’exploitation.[cite:1]

## Architecture globale

```text
Internet
   │
   ├── Hébergement web front
   │    ├── rennesdev.fr
   │    ├── api.rennesdev.fr
   │    └── test.rennesdev.fr
   │
   └── VPS
        ├── Nginx
        │
        ├── API principale Rennesdev
        │    ├── chemin : /home/manu/var/www/api-rennesdev-backend
        │    ├── mode : systemd + Uvicorn
        │    └── port local : 8001
        │
        ├── diagnostic-api
        │    ├── mode : conteneur Docker
        │    ├── rôle : mini-service de diagnostic fiscal en ligne
        │    └── port : 8000
        │
        ├── n8n
        │    ├── mode : conteneur Docker
        │    └── port : 5678
        │
        └── Archives
             └── /var/archives/api-rennesdev-backend.archive-2026-06-18-0754
```

## Ports utilisés

| Port | Service | Usage |
|---|---|---|
| 8000 | `diagnostic-api` | Service Docker de diagnostic fiscal en ligne [cite:1] |
| 8001 | `api-rennesdev` | API principale Rennesdev via systemd + Uvicorn [cite:1] |
| 5678 | `n8n` | Automatisations n8n en Docker [cite:1] |
| 8100 | `facturx-api` | Ancien service Factur-X, supprimé [cite:1] |

Le **port 8000** est donc bien occupé par `diagnostic-api`, ce qui explique pourquoi il ne doit pas être considéré comme libre sur le VPS.[cite:1]

## Diagnostic-api

`diagnostic-api` n’est pas une brique technique centrale de l’API Rennesdev : c’est un service web simple, utilisé pour un diagnostic en ligne, avec une logique liée au sujet de la facture électronique et de la réforme fiscale à venir.[cite:1]

Le garder encore quelque temps est cohérent, car la réforme de la facturation électronique entre en vigueur à partir du **1er septembre 2026** pour la réception des factures électroniques par toutes les entreprises, avec émission obligatoire dès cette date pour les grandes entreprises et ETI.[web:28][web:31][web:34]

Pour les PME et micro-entreprises, l’obligation d’émission est prévue au **1er septembre 2027**, mais la réception électronique devient bien un sujet général dès le **1er septembre 2026**.[web:28][web:32]

## État actuel

La lecture opérationnelle du serveur est maintenant simple :

- `/home/manu/var/www/api-rennesdev-backend` = vraie production API Rennesdev ; [cite:1]
- port 8001 = API principale Rennesdev ; [cite:1]
- port 8000 = `diagnostic-api` ; [cite:1]
- port 5678 = `n8n` ; [cite:1]
- `/var/www/api-rennesdev-backend` = ancienne copie archivée ; [cite:1]
- `facturx-api` = supprimé.[cite:1]
