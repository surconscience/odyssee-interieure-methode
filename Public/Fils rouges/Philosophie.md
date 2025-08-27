---
layout: single
title: Philosophie
description: Perspectives philosophiques sur le développement personnel et spirituel
permalink: /fils-rouges/philosophie/
toc: false
toc_sticky: false
type: fil_rouge
---
Les grecs ont inventé le mot *philosophia* qui veut dire `« amour de la sagesse »`. Pourtant, à l'école, nous avons appris la philosophie à travers des constructions assez abstraites et complexes.

Comment dépasser cela et retrouver une approche pratique et abordable de la philosophie ?
## Chemins associés

{% assign chemins_lies = site.pages | where: "type", "chemin" | where: "fil_rouge", page.title %}
<ul>
  {% for chemin in chemins_lies %}
    <li><a href="{{ chemin.url }}">{{ chemin.title }}</a></li>
  {% endfor %}
</ul>

