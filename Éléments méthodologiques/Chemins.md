## Mécanisme des Chemins

Les Chemins sont des explorations plus spécifiques. Ils sont connectés entre eux ainsi qu'à un ou plusieurs [[Éléments méthodologiques/Fils rouges|fils rouges]].
## Structure technique

Les fichiers de Chemins, situés dans le répertoire `Public/Chemins/` au sein de votre vault Obsidian, sont structurés comme suit :
- Frontmatter (en YAML) avec les métadonnées suivantes :
  - `layout: single` (utilisé pour l'affichage sur le site Jekyll, généralement `single`)
  - `title: "Le Titre de Votre Chemin"` (sera affiché comme titre principal de la page)
  - `permalink: /chemins/nom-unique-du-chemin/` (définit l'URL de la page sur le site, ex: `/chemins/5_elements/`)
  - `description: "Une brève description du contenu du chemin."` (utilisée pour les aperçus et les métadonnées SEO du site)
  - `toc: false` (par défaut, la table des matières n'est pas affichée. Mettre à `true` pour l'activer si besoin.)
  - `toc_sticky: false` (si `toc: true`, mettre également à `true` pour que la table des matières reste visible en haut lors du défilement. Par défaut à `false`.)
  - `classes: wide` (optionnel, peut être utilisé pour des mises en page spécifiques du thème Minimal Mistakes, comme `wide`)
  - `type: chemin` (essentiel pour identifier ce contenu comme un chemin, notamment pour les requêtes Dataview)
  - `fil_rouge: "Nom du Fil Rouge"` (indique le [[Éléments méthodologiques/Fils rouges|Fil rouge]] principal auquel ce chemin est associé. Ce champ peut contenir le nom d'un seul fil rouge ou une liste de noms si le chemin est pertinent pour plusieurs fils.)
- Contenu principal en Markdown, qui commence typiquement par une section `## Description générale`, suivie d'autres sections pertinentes au chemin.

## Liste des Chemins

```dataview
TABLE WITHOUT ID
  file.link as "Chemins",
  fil_rouge as "Fil Rouge Associé"
FROM ""
WHERE type = "chemin"
SORT file.name ASC
```
