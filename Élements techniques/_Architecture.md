Cette note décrit la **vision technique** d’ensemble pour publier l’Odyssée Intérieure (méthode et contenu) à partir de fichiers Obsidian vers la plateforme en ligne **surconscience.net**. 

L’architecture se veut **évolutive** pour s’adapter aux futurs développements du projet.

## Hypothèses initiales

- **Outil de base** : Obsidian, où se trouvent toutes les notes (constats, méthodes, liens).
- **Portion publiable** : une sélection de notes (ex. le manifeste, les textes suffisamment aboutis).
- **Long terme** : un site **semi-automatisé** ou automatisé, avec un pipeline d’exportation (Markdown → HTML) et un déploiement continu (CI/CD) et la possibilité d'avoir de nombreux contributeurs.
- **Évolutivité** : la structure pourra se complexifier (ajout de commentaires, d’IA, multi-langue…) au fil du temps.

## Éléments utilisés

1. **[[Jekyll]]**
    - [[Générateur de site statique]] en [[Ruby]]
    - Transforme les `.md` en pages HTML, gère la navigation et le style
    - Excellent support Markdown et intégration GitHub Pages
2. **Pipeline CI/CD**
    - Intègre la conversion (Markdown → HTML),
    - Gère le déploiement automatique sur le serveur (LAMP),
    - Pourrait inclure un appel à l’IA (Windsurf) pour correction/traduction/résumé.
3. **Hébergement LAMP**
    - Permet d’héberger des pages statiques (HTML/CSS/JS),
    - Possibilité de scripts PHP/MySQL si besoin d’ajouts dynamiques (dans le futur).

## Flux de travail (version de base)

1. **Rédaction et mise à jour** dans Obsidian.
2. **Sélection** des notes publiables (via tags, dossiers, ou un script dédié).
3. **Conversion** en local ou via un serveur CI/CD (Markdown → HTML).
4. **Déploiement** sur le serveur (FTP, Git hooks, ou pipeline automatisé).

## Rôle de l’IA (Windsurf)

1. **Avant publication** : correction du style, enrichissement (résumés, extraits).
2. **Au moment du build** : script qui appelle l’IA pour générer du texte complémentaire.
3. **Évolutions futures** : fonctionnalité dynamique (mais impliquerait un backend différent).

## Questions ouvertes

1. Quelle **structure** adopter pour séparer contenu privé / contenu publiable ?
2. Quelle **solution** de CI/CD est la plus adaptée (GitLab CI, GitHub Actions, hooks sur le mutualisé…) ?
3. Comment gérer la **navigation** (catégorisation par lignes de métro / bus / routes) pour que cela reste clair sur le site final ?
4. À quel point l’IA sera-t-elle intégrée (process ponctuel ou composante clé) ?

## Liens internes

- [[Manifeste - Appel aux artisans de la surconscience]] – Exemple de note destinée à la publication.
- [[Filtrage des constats]] – Comment trier contenu privé/public.

## Attributs

- **Seuil** : Non
- **Chemins** : #architecture, #publication
- **Porte** : Entrée