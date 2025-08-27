<!-- SECTION VISIBLE DANS OBSIDIAN -->
## Constats associés
```dataviewjs
// Importer le module de fonctions DataviewJS
const dvFiches = await dv.view("Éléments méthodologiques/partials/obsidian-dv-fiches");

// Utiliser la fonction pour afficher les constats associés à ce chemin
// Remplacer "Titre du chemin" par le titre exact du chemin
dvFiches.afficherConstatsAssocies(dv.current().file.frontmatter.title);
```

<!-- SECTION VISIBLE DANS JEKYLL -->
{% comment %}Ne pas modifier cette section - Code pour Jekyll{% endcomment %}
## Constats associés à "{{ page.title }}"

{% assign constats_lies = site.pages | where: "type", "constat" | where: "chemin_associe", page.title | sort: "sequence" %}
<ul>
  {% for constat in constats_lies %}
    <li><a href="{{ constat.url }}">{{ constat.title }}</a></li>
  {% endfor %}
</ul>