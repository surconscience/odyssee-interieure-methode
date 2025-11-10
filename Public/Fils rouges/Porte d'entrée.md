---
layout: single
title: Porte d'entrée
permalink: /fils-rouges/porte-dentre
description: Vos premiers pas dans l'Odyssée intérieure.
toc: false
toc_sticky: false
classes: wide
type: fil_rouge
---
Ceci est la porte d'entrée de l'[[Odyssée intérieure]]. Elle vous donnera accès à tout le contenu au moment adéquat, selon vos prises de conscience et selon vos souhaits.
## Chemins associés
```dataviewjs
// Récupérer les chemins associés
const currentPage = dv.current();
const chemins = dv.pages("")
  .where(p => p.type === "chemin" && p.fil_rouge === currentPage.title);
// Générer la liste de liens
dv.list(chemins.file.link);
```
<div class="jekyll-only" markdown="0">
{% assign chemins_lies = site.pages | where: "type", "chemin" | where: "fil_rouge", page.title %}
<ul>
  {% for chemin in chemins_lies %}
    <li><a href="{{ chemin.url }}">{{ chemin.title }}</a></li>
  {% endfor %}
</ul>
</div>
