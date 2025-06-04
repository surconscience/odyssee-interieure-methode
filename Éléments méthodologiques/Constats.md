## Mécanisme des Constats

Les Constats sont des étapes dans un raisonnement sur un chemin. Ils peuvent être des principes, des faits observés, ou des conclusions issues d'une réflexion. Un constat est souvent une unité d'information concise et impactante.

Ils peuvent être autonomes ou liés à des [[Chemins]] et/ou des [[Fils rouges|fils rouges]] pour fournir un contexte plus large.
## Structure technique

Les fichiers de Constats, situés dans le répertoire `Public/Constats/` au sein de votre vault Obsidian, sont structurés comme suit :
- Frontmatter (en YAML) avec les métadonnées suivantes :
  - `layout: single` (utilisé pour l'affichage sur le site Jekyll, généralement `single`)
  - `title: "Le Titre de Votre Constat"` (sera affiché comme titre principal de la page)
  - `description: "Une brève description du contenu du constat."` (utilisée pour les aperçus et les métadonnées SEO du site)
  - `permalink: /constats/nom-unique-du-constat/` (définit l'URL de la page sur le site, ex: `/constats/nom-du-constat/`)
  - `toc: false` (par défaut, la table des matières n'est pas affichée)
  - `toc_sticky: false` (par défaut, la table des matières n'est pas "collante")
  - `type: constat` (essentiel pour identifier ce contenu comme un constat, notamment pour les requêtes Dataview)
  - `chemin_associe: "Nom du Chemin"` (Optionnel. Indique le [[Chemins|Chemin]] principal auquel ce constat est associé. Peut être une chaîne de caractères pour un seul chemin, ou une liste YAML pour plusieurs.)
  - `fil_rouge_associe: "Nom du Fil Rouge"` (Optionnel. Indique le [[Fils rouges|Fil rouge]] principal auquel ce constat est associé. Peut être une chaîne de caractères pour un seul fil rouge, ou une liste YAML pour plusieurs.)
- Contenu principal en Markdown, qui développe le constat.

## Liste des Constats

```dataview
TABLE WITHOUT ID
  file.link as "Constats",
  chemin_associe as "Chemin Associé",
  fil_rouge_associe as "Fil Rouge Associé"
FROM "Public/Constats"
WHERE type = "constat"
SORT file.name ASC
```
