# Configuration Git-GitHub pour Odyssée Intérieure

## Structure du dépôt

Le projet Odyssée Intérieure utilise Git et GitHub avec une configuration spéciale permettant de suivre tous les fichiers localement tout en ne publiant qu'une partie sélectionnée sur GitHub.

### Branches

Le dépôt utilise deux branches principales :

1. **main** - Contient l'ensemble du projet avec tous les fichiers
2. **public** - Contient uniquement le répertoire Public et les fichiers essentiels (README.md, LICENSE.md, .gitignore)

## Flux de travail

### Travailler sur le projet complet

Pour travailler sur l'ensemble du projet avec tous les fichiers :

```bash
git checkout main
# Faire des modifications
git add .
git commit -m "Description des changements"
git push
```

### Mettre à jour la branche publique

Après avoir fait des modifications dans le répertoire Public ou dans les fichiers essentiels que vous souhaitez publier :

```bash
# Assurez-vous d'être sur main et que vos changements sont commités
git checkout main
git add .
git commit -m "Description des changements"
git push

# Puis mettez à jour la branche public
git checkout public
git merge main
git push
```

### Vérifier ce qui est publié

Pour voir exactement ce qui est visible publiquement sur GitHub :

```bash
git checkout public
# Explorez les fichiers
git checkout main  # Pour revenir à la version complète
```

## Licence

Le projet est sous licence [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.fr).

## URL du dépôt GitHub

Le projet est hébergé sur GitHub à l'adresse suivante :
https://github.com/surconscience/odyssee-interieure-methode

## Avantages de cette configuration

1. **Séparation du contenu** : Vous pouvez continuer à travailler sur tous vos fichiers localement dans la branche "main"
2. **Publication sélective** : Seul le contenu du répertoire "Public" est visible dans la branche "public" sur GitHub
3. **Flexibilité** : Vous pouvez facilement basculer entre les deux branches selon vos besoins
4. **Sécurité** : Les fichiers de travail et notes personnelles restent privés

## Conseils pour Obsidian

Cette configuration est particulièrement adaptée à Obsidian, car elle vous permet de :
- Garder vos notes personnelles et votre travail en cours dans la branche main
- Publier uniquement les notes finalisées dans le répertoire Public
- Utiliser Git pour suivre les modifications de toutes vos notes
- Avoir une sauvegarde complète de votre vault Obsidian

## Configuration initiale (pour référence)

Si vous devez recréer cette configuration sur un autre projet :

1. Initialiser un dépôt Git : `git init`
2. Créer et pousser la branche main : `git add .`, `git commit -m "Initial commit"`, `git push -u origin main`
3. Créer la branche public : `git checkout -b public`
4. Supprimer les fichiers non publics : `git rm -r [fichiers/dossiers à ne pas publier]`
5. Commit et push : `git commit -m "Configuration branche public"`, `git push -u origin public`
