let personne = {
    nom: "Alice",
    age: 30,
    adresse: {
        rue: "Rue de la Paix",
        ville: "Paris",
        codePostal: 75000
    },
    hobbies: ["Lecture", "Natation", "Voyages"]
};

console.log(personne.nom);
console.log(personne.age);
console.log(personne.adresse.rue);
console.log(personne.adresse.ville);
console.log(personne.adresse.codePostal);
console.log(personne.hobbies);

personne.hobbies.push("Cuisine");
personne.age = 31;
delete personne.adresse.codePostal;

console.log(personne);
