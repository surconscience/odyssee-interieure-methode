---
layout: single
title: Intérêts et limites de la philosophie
permalink: /chemins/interets-limites-philosophie/
description: Exploration de la valeur et des bornes de la démarche philosophique dans le cadre de l'Odyssée intérieure.
toc: false
toc_sticky: false
classes: wide
type: chemin
fil_rouge: Philosophie
---
## Description générale

Pourquoi s'intéresser à la philosophie? Quels sont les points d'attention principaux pour une approche surconsciente de la philosophie ? 
## Constats associés

{% assign constats_lies = site.pages | where: "type", "constat" | where: "chemin_associe", page.title | sort: "sequence" %}
<ul>
  {% for constat in constats_lies %}
    <li><a href="{{ constat.url }}">{{ constat.title }}</a></li>
  {% endfor %}
</ul>