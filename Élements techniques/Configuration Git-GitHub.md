## Structure du dépôt

Le projet Odyssée intérieure utilise Git et GitHub pour le contrôle de version et le partage du contenu.

### Branche principale

Le dépôt utilise une seule branche principale :

**main** - Contient l'ensemble du projet avec tous les fichiers et est synchronisée avec GitHub

## Flux de travail

### Travailler sur le projet

Pour travailler sur le projet et synchroniser avec GitHub :

```bash
# S'assurer d'être sur la branche main
git checkout main

# Faire des modifications localement

# Ajouter les fichiers modifiés
git add .

# Créer un commit avec une description claire
git commit -m "Description des changements"

# Pousser les changements vers GitHub
git push
```

### Récupérer les changements depuis GitHub

Pour récupérer les changements effectués par d'autres ou depuis un autre ordinateur :

```bash
git pull
```

## Licence

Le projet est sous licence [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.fr).

## URL du dépôt GitHub

Le projet est hébergé sur GitHub à l'adresse suivante :
https://github.com/surconscience/odyssee-interieure-methode

## Avantages de cette configuration

1. **Simplicité** : Une seule branche à gérer, flux de travail Git standard
2. **Transparence** : Tout le contenu est visible et accessible sur GitHub
3. **Collaboration** : Facilite la contribution d'autres personnes au projet
4. **Intégration** : S'intègre parfaitement avec d'autres outils et services

## Conseils pour Obsidian

Cette configuration est particulièrement adaptée à Obsidian, car elle vous permet de :
- Utiliser Git pour suivre les modifications de toutes vos notes
- Avoir une sauvegarde complète de votre vault Obsidian sur GitHub
- Partager facilement votre travail avec d'autres
- Intégrer votre contenu avec d'autres outils comme Jekyll

## Configuration initiale (pour référence)

Si vous devez recréer cette configuration sur un autre projet :

1. Initialiser un dépôt Git : `git init`
2. Créer la branche main localement : `git add .`, `git commit -m "Initial commit"`
3. Créer un dépôt sur GitHub avec le même nom
4. Connecter le dépôt local au dépôt distant : `git remote add origin https://github.com/username/repository.git`
5. Pousser le contenu vers GitHub : `git push -u origin main`
