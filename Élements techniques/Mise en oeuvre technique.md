## Objectif
La mise en œuvre technique vise à structurer l'Odyssée intérieure sous une forme exploitable dans Obsidian.

## 1. Organisation des fichiers et dossiers
L'organisation des fichiers suit une hiérarchie en trois niveaux, facilitant la navigation et la structuration des idées :

- **`📂 Odyssée intérieure`** (Dossier racine)
    - `📂 Ligne de métro X` → Contient les grandes lignes directrices structurantes correspondant aux fils rouges principaux
        - `📂 Ligne de bus Y` → Contient les chemins structurants correspondant aux fils rouges d'importance intermédiaire
            - `📂 Route Z` → Contient les constats spécifiques pour les chemins de base

Chaque note de constat est placée dans un chemin correspondant, permettant une hiérarchie claire tout en assurant l'interconnexion des concepts via des liens internes `[[Nom du constat]]`.

Les **seuils**, **fils rouges** et **portes** sont des **attributs** spécifiques aux constats, permettant d’organiser la visualisation et les relations dans le graphe d’Obsidian.
## 2. Utilisation des fonctionnalités d'Obsidian

### Liens entre les notes
- Chaque constat est lié à d’autres constats pour former un réseau dynamique.
- Les seuils sont des constats particuliers indiquant un changement de compréhension significatif.
- Les fils rouges sont des liens thématiques qui permettent de structurer l'exploration selon différentes perspectives.
- Les portes sont des constats marquant les débuts et fins de chemins spécifiques dans le réseau de réflexion.

### Graphe de visualisation
- **Personnalisation** : Activer les options d'affichage pour différencier les types de notes (tags ou couleurs).
- **Navigation** : Utiliser le mode interactif pour explorer les connexions entre les concepts.
- **Filtrage** : Afficher uniquement les constats liés à un fil rouge spécifique en utilisant les requêtes de **Dataview** ou les filtres du graphe.

### Plugins recommandés
- **Dataview** : Génération automatique de listes de constats avec filtrage selon les seuils, fils rouges et portes.
- **Juggl** : Amélioration du graphe pour une meilleure visualisation.
- **Templater** : Création de modèles standardisés pour chaque type de note.
 
## 3. Structuration des notes
### Modèle de note pour un constat

```markdown
# Titre du Constat

## Description
Brève explication du constat.

## Liens avec d'autres constats
- [[Constat A]]
- [[Constat B]]

## Attributs
- **Seuil** : Oui/Non
- **Fils rouges** : #fil-rouge-x, #fil-rouge-y
- **Porte** : Entrée/Sortie (si applicable)
```

L’ajout d’attributs sous forme de **tags** (`#seuil`, `#fil-rouge-x`, `#porte-entree`, `#porte-sortie`) permet d'afficher les constats liés à un fil rouge ou de filtrer les seuils et les portes dans la visualisation.