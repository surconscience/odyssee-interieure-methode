# Intégration Obsidian-Jekyll pour Odyssée Intérieure

## Vue d'ensemble

Ce document explique comment le projet Odyssée Intérieure intègre Obsidian (pour la prise de notes et la création de contenu) avec Jekyll (pour la publication web) via Git.

## Architecture globale

L'architecture d'intégration repose sur trois composants principaux :

1. **Obsidian** : Environnement de travail principal pour la création et l'organisation des notes
2. **Git** : Système de contrôle de version pour suivre les modifications et synchroniser avec GitHub
3. **Jekyll** : Générateur de site statique pour publier le contenu sur le web

## Configuration des liens symboliques

Pour éviter la duplication de contenu entre Obsidian et Jekyll, nous utilisons des liens symboliques qui permettent de maintenir les fichiers à un seul endroit tout en les rendant accessibles depuis les deux environnements.

### Structure des répertoires

```
/home/oliver/Nextcloud/Oliver/01_philosophie_spiritualité/Odyssée intérieure_méthode/
├── Public/                  # Répertoire contenant les notes à publier
│   ├── Manifeste.md
│   ├── Odyssée intérieure.md
│   └── ...
└── Élements techniques/     # Documentation technique

/home/oliver/WebDev/Sites/surconscience.net/
├── _config.yml              # Configuration Jekyll
├── public-posts/
│   ├── vault1/              # Contient des liens symboliques vers le répertoire Public d'Obsidian
│   └── vault2/
└── ...
```

### Création des liens symboliques

Les liens symboliques sont créés entre le répertoire Public d'Obsidian et le répertoire vault1 de Jekyll :

```bash
# Exemple de commande pour créer un lien symbolique
ln -s /chemin/vers/Obsidian/Public/fichier.md /chemin/vers/Jekyll/public-posts/vault1/fichier.md
```

## Structure des fichiers Markdown

Pour que les fichiers Markdown d'Obsidian soient correctement interprétés par Jekyll, chaque fichier dans le répertoire Public doit contenir un en-tête YAML au début :

```yaml
---
layout: page
title: "Titre de la page"
---
```

### Conversion des liens Wiki d'Obsidian

Obsidian utilise la syntaxe `[[Nom du lien]]` pour les liens internes, mais Jekyll ne comprend pas cette syntaxe par défaut. Deux approches sont possibles :

1. **Conversion manuelle** : Remplacer les liens Wiki par des liens Markdown standard `[Texte du lien](URL)`
2. **Plugin Jekyll** : Utiliser un plugin Jekyll qui interprète la syntaxe des liens Wiki d'Obsidian

## Configuration Jekyll

Le fichier `_config.yml` de Jekyll est configuré pour inclure les répertoires contenant les liens symboliques :

```yaml
include:
  - public-posts/vault1
  - public-posts/vault2
```

De plus, une collection peut être définie pour organiser le contenu :

```yaml
collections:
  surconscience:
    output: true
    permalink: /:collection/:name
```

## Flux de travail

1. **Création et édition de contenu** dans Obsidian
2. **Ajout de l'en-tête YAML** aux fichiers destinés à être publiés
3. **Commit et push** des modifications vers GitHub via Git
4. **Génération du site** avec Jekyll (`bundle exec jekyll serve` pour prévisualiser localement)

## Avantages de cette configuration

1. **Environnement de travail unifié** : Utilisation d'Obsidian pour toute la création de contenu
2. **Pas de duplication** : Les fichiers existent à un seul endroit grâce aux liens symboliques
3. **Contrôle de version** : Suivi des modifications avec Git
4. **Publication sélective** : Seuls les fichiers dans le répertoire Public sont publiés
5. **Prévisualisation locale** : Possibilité de prévisualiser le site avant publication

## Dépannage

### Problèmes courants avec les liens symboliques

- **Liens brisés** : Vérifier que les chemins sont corrects et que les fichiers existent
- **Permissions** : S'assurer que les permissions sont correctes pour les fichiers et répertoires

### Problèmes courants avec Jekyll

- **En-têtes YAML manquants** : Vérifier que chaque fichier commence par un en-tête YAML valide
- **Liens Wiki non convertis** : Vérifier que les liens Wiki sont correctement gérés
