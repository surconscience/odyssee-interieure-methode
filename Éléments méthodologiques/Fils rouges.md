## Mécanisme des fils rouges

Les fils rouges sont des parcours thématiques qui traversent l'ensemble de la méthode de l'Odyssée intérieure. Ils permettent d'explorer une dimension importante et structurante.

## Structure technique

Les fichiers de fils rouges, situés dans le répertoire `Public/Fils rouges/` au sein de votre vault Obsidian, sont structurés comme suit :
- Frontmatter (en YAML) avec les métadonnées suivantes :
  - `layout: single` (utilisé pour l'affichage sur le site Jekyll, généralement `single`)
  - `title: "Le Titre de Votre Fil Rouge"` (sera affiché comme titre principal de la page)
  - `description: "Une brève description du contenu du fil rouge."` (utilisée pour les aperçus et les métadonnées SEO du site)
  - `permalink: /fils-rouges/nom-unique-du-fil-rouge/` (définit l'URL de la page sur le site)
  - `toc: false` (mettre à `true` pour afficher une table des matières sur la page)
  - `toc_sticky: false` (mettre à `true` si la table des matières doit rester visible en haut de la page lors du défilement)
  - `type: fil_rouge` (essentiel pour identifier ce contenu comme un fil rouge, notamment pour les requêtes Dataview)
  - (Optionnel, si pertinent) `date: YYYY-MM-DD` (peut être utilisé pour une date de création ou de dernière mise à jour significative)
- Contenu principal en Markdown, qui commence typiquement par une section `## Description générale`.

## Liste des fils rouges

```dataview
TABLE WITHOUT ID
  file.link as "Fils rouges"  
FROM ""  
WHERE type = "fil_rouge"
SORT file.name ASC
```
