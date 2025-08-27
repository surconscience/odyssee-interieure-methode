---
---

```dataviewjs
// Fonction pour afficher les constats associés à un chemin
function afficherConstatsAssocies(cheminTitre) {
  const constats = dv.pages("")
    .where(p => p.type === "constat" && p.chemin_associe === cheminTitre)
    .sort(p => p.sequence);
  
  dv.list(constats.file.link);
}

// Exporter la fonction pour qu'elle soit accessible
module.exports = {
  afficherConstatsAssocies
}
```
