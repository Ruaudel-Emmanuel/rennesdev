Site web RennesDev

Site statique officiel de RennesDev, l'activité de freelance d'Emmanuel Ruaudel.



Ce projet est un site web léger en HTML/CSS axé sur :



un positionnement clair pour les PME et les indépendants,

de meilleures bases pour le SEO technique,

une maintenance et un déploiement simplifiés,

une compatibilité avec les environnements d'hébergement statique standards comme Infomaniak.

Objectif du projet

Le site promeut des services de freelance autour de :



l'automatisation en Python,

l'intégration d'API,

l'automatisation de workflows,

les tableaux de bord et outils opérationnels,

l'optimisation des processus pour les petites entreprises.



Le site est conçu pour rester simple, rapide, lisible et facile à mettre à jour, sans framework.



Stack technique actuelle

HTML5

CSS3

Assets statiques

Intégration de formulaire Tally

Google Tag Manager

Données structurées JSON-LD

Aucun framework JavaScript, aucune étape de build, aucun backend requis.



Structure des fichiers

rennesdev.fr/

├── index.html

├── portofolio.html

└── assets/

&#x20;   ├── css/

&#x20;   │   └── style.css

&#x20;   └── img/

&#x20;       └── banniere-codeur.jpg

Chemins importants

Le site étant déployé selon cette structure, les chemins vers les assets doivent y correspondre exactement.



Dans index.html

CSS :



<link rel="stylesheet" href="./assets/css/style.css">

Image d'en-tête (Hero) :



<img src="./assets/img/banniere-codeur.jpg" alt="" class="hero\_\_bg">

Image de prévisualisation pour les réseaux sociaux :



<meta property="og:image" content="https://rennesdev.fr/assets/img/banniere-codeur.jpg">

<meta name="twitter:image" content="https://rennesdev.fr/assets/img/banniere-codeur.jpg">

Améliorations SEO incluses

La version actuelle comprend :



une balise title unique,

une méta-description,

une URL canonique,

des balises Open Graph,

des balises Twitter Card,

des données structurées de type ProfessionalService,

une structure de section sémantique,

une navigation interne par ancres,

des titres orientés services,

une intention locale (Rennes et Bretagne).



Ces éléments favorisent le SEO technique, la clarté du contenu et une meilleure interprétation des pages par les moteurs de recherche. \[web:83]\[web:86]



Navigation

Le menu de navigation principal renvoie actuellement vers :



Services

Portfolio

À propos

Contact

Si la page Portfolio conserve son nom de fichier actuel, utilisez :

