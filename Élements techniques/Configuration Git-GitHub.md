# Configuration Git-GitHub pour Odyssée Intérieure

## Structure du dépôt

Le projet Odyssée Intérieure utilise Git et GitHub avec une configuration spéciale permettant de suivre tous les fichiers localement tout en ne publiant qu'une partie sélectionnée sur GitHub.

### Branches

Le dépôt utilise deux branches principales :

1. **main** - Existe uniquement en local et contient l'ensemble du projet avec tous les fichiers
2. **public** - Seule branche visible sur GitHub, contient uniquement le répertoire Public et les fichiers essentiels (README.md, LICENSE.md, .gitignore)

## Flux de travail

### Travailler sur le projet complet

Pour travailler sur l'ensemble du projet avec tous les fichiers :

```bash
git checkout main
# Faire des modifications
git add .
git commit -m "Description des changements"
# Pas besoin de push, la branche main n'existe que localement
```

### Mettre à jour la branche publique

Après avoir fait des modifications dans le répertoire Public ou dans les fichiers essentiels que vous souhaitez publier :

```bash
# Assurez-vous d'être sur main et que vos changements sont commités
git checkout main
git add .
git commit -m "Description des changements"
# Pas de push pour main car elle n'existe qu'en local

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
2. Créer la branche main localement : `git add .`, `git commit -m "Initial commit"`
3. Créer la branche public : `git checkout -b public`
4. Supprimer les fichiers non publics : `git rm -r [fichiers/dossiers à ne pas publier]`
5. Commit et push de la branche public : `git commit -m "Configuration branche public"`, `git push -u origin public`
6. Définir la branche public comme branche par défaut sur GitHub
7. Si nécessaire, supprimer la branche main de GitHub (mais pas localement) : `git push origin --delete main`
