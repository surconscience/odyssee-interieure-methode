---
layout: single
title: La porte des nombres
permalink: /chemins/porte-des-nombres/
description: Pourquoi l'étude des nombres est-elle si importante?
toc: false
toc_sticky: false
classes: wide
type: chemin
fil_rouge: Nombres
---
Comment entrer dans l'étude de nombres ? Des premiers constats permettent d'initier le chemin.
## Constats associés
```dataviewjs
// Récupérer les constats associés
const currentPage = dv.current();
const constats = dv.pages("")
  .where(p => p.type === "constat" && p.chemin_associe === currentPage.title)
  .sort(p => p.sequence);

// Générer la liste de liens
dv.list(constats.file.link);
```

<div class="jekyll-only" markdown="0">
{% assign constats_lies = site.pages | where: "type", "constat" | where: "chemin_associe", page.title | sort: "sequence" %}
<ul>
  {% for constat in constats_lies %}
    <li><a href="{{ constat.url }}">{{ constat.title }}</a></li>
  {% endfor %}
</ul>
</div>
