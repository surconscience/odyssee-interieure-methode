---
fil_rouge: Porte d'entrée
title: Le premier jour
permalink: /chemins/premier-jour/
description: Sommes-nous éveillés ou endormis ?
toc: false
toc_sticky: false
classes: wide
type: chemin
layout: single
---
L'expérience du "premier jour" ouvre la porte à l'ensemble de l'odyssée intérieure. Et vous? Avez-vous déjà eu votre premier jour ?
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
