# Fils rouges

## Mécanisme des fils rouges

Les fils rouges sont des parcours thématiques qui traversent l'ensemble de la méthode de l'Odyssée intérieure. Ils permettent d'explorer une dimension importante et structurante.

Chaque fil rouge :
- Est décrit dans un fichier dédié dans le répertoire "Fils rouges"
- Contient des métadonnées YAML pour identifier son type

## Structure technique

Les fichiers de fils rouges sont structurés comme suit :
- Frontmatter avec métadonnées :
  - `type: fil_rouge`
  - `title`, `date`, `description`
- Description générale du fil rouge

## Liste des fils rouges

```dataview
TABLE WITHOUT ID
  file.link as "Fils rouges"  
FROM ""  
WHERE type = "fil_rouge"
SORT file.name ASC
```
