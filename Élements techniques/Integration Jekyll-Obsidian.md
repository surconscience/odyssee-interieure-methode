---
title: Intégration Jekyll-Obsidian
---
# Intégration Jekyll-Obsidian

Ce document explique le mécanisme d'intégration entre Obsidian et Jekyll pour les listes dynamiques de contenus (fils rouges, parcours thématiques, etc.).

## Architecture générale

Notre système repose sur deux composants principaux :
- **Obsidian** : pour la rédaction et l'organisation des contenus
- **Jekyll** : pour la génération du site web

Le contenu créé dans Obsidian est rendu disponible pour Jekyll via des liens symboliques (symlinks) :
- Le dossier `Public/` d'Obsidian est accessible dans Jekyll via `public-posts/vault1`
- Les contenus spéciaux (comme les fils rouges) sont placés dans des sous-dossiers dédiés

## Mécanisme de génération des listes dynamiques

Pour générer des listes dynamiques de contenus (comme les fils rouges, parcours thématiques, etc.), nous utilisons un **plugin Ruby personnalisé** plutôt que les collections Jekyll standards.

### Pourquoi cette approche ?

1. **Cohérence unique** : Tous les contenus restent dans Obsidian, sans duplication
2. **Flexibilité** : Le plugin peut générer des URLs propres et normaliser les accents/espaces
3. **Simplicité** : Un simple tag Liquid suffit pour insérer une liste complète et formatée

### Fonctionnement technique

1. **Tag Liquid dans la page Markdown** :
   ```liquid
   {% nom_du_tag %}
   ```

2. **Plugin Ruby dans Jekyll** :
   - Situé dans `_plugins/nom_du_tag.rb`
   - Scanne le dossier approprié via le symlink (`public-posts/vault1/...`)
   - Génère le HTML de la liste (tableau, liste à puces, etc.)

3. **Rendu final** :
   - Le tag est remplacé par le HTML généré lors du build Jekyll
   - Dans Obsidian, le tag reste visible mais n'interfère pas avec la lecture

## Exemple : Fils Rouges

Les fils rouges illustrent parfaitement ce mécanisme :

1. **Stockage** : Les fichiers des fils rouges sont dans Obsidian sous `/Public/Fils rouges/`
2. **Access Jekyll** : Via le symlink `public-posts/vault1/Fils rouges`
3. **Génération** : Le plugin `fils_rouges_tag.rb` :
   - Scanne les fichiers `.md` dans ce dossier
   - Génère des URLs propres (`/fils-rouges/nom-du-fil/`)
   - Crée un tableau HTML avec titres et descriptions

## Comment ajouter un nouveau type de liste

Pour créer un nouveau type de liste dynamique (ex : parcours, pratiques, etc.) :

1. **Créer un plugin** basé sur le modèle existant :
   ```ruby
   module Jekyll
     class NouveauTag < Liquid::Tag
       def render(context)
         site = context.registers[:site]
         # Chemin vers le dossier des contenus
         dossier = File.join(site.source, "public-posts", "vault1", "_dossier_specifique")
         # [Code de génération similaire à fils_rouges_tag.rb]
       end
     end
   end
   Liquid::Template.register_tag('nouveau_tag', Jekyll::NouveauTag)
   ```

2. **Créer une page** avec le tag correspondant :
   ```markdown
   ---
   title: Nouveau Type de Contenu
   ---
   # Liste des contenus
   
   {% nouveau_tag %}
   ```

## Points importants à retenir

- Les modifications dans Obsidian sont automatiquement reflétées sur le site après rebuild
- Pas besoin de dupliquer les fichiers entre Obsidian et Jekyll
- Pour que les pages individuelles fonctionnent, les URLs générées doivent correspondre aux permalinks Jekyll
- Un rebuild complet de Jekyll est nécessaire après l'ajout de nouveaux fichiers
