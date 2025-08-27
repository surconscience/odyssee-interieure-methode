---
layout: single
title: Nombres
permalink: /fils-rouges/nombres/
description: La porte des nombres.
toc: false
toc_sticky: false
classes: wide
type: fil_rouge
---
Dans ce fil rouge, nous allons passer la porte des Nombres. Le sujet est complexe et ne peut être transmis simplement. De nombreuses méditations et observations personnelles seront nécessaires pour arriver à en intérioriser le contenu initiatique et pratique.

Cependant, il est inévitable de s'y confronter à un moment ou un autre du chemin et il ouvre des portes sur des enseignements très puissants.
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
