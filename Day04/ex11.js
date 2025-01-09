let livre = {
    titre: "Le Petit Prince",
    auteur: "Antoine de Saint-Exupéry",
    annee: 1943,
    disponible: true
};

console.log(livre.titre);
console.log(livre.auteur);
console.log(livre.annee);
console.log(livre.disponible);

livre.disponible = false;
livre.langue = "Français";

console.log(livre);
