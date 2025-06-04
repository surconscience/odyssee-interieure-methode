---
layout: single
title: Philosophie
description: Perspectives philosophiques sur le développement personnel et spirituel
permalink: /fils-rouges/philosophie/
toc: false
toc_sticky: false
type: fil_rouge
---
Les grecs ont inventé le mot *philosophia*, qui veut dire `« amour de la sagesse »`. Pourtant, à l'école, nous avons appris « des philosophes » plutôt que « la philosophie » et souvent à travers des constructions assez abstraites.

Comment retrouver et mettre en pratique concrètement cet amour de la sagesse ? 

[[Philosophie école de sagesse|PASSEZ LE PORTAIL !]]
## Chemins associés

{% assign chemins_lies = site.pages | where: "type", "chemin" | where: "fil_rouge", page.title %}
<ul>
  {% for chemin in chemins_lies %}
    <li><a href="{{ chemin.url }}">{{ chemin.title }}</a></li>
  {% endfor %}
</ul>

