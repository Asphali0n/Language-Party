let etudiants = [
    { nom: "Alice", age: 20, note: 14 },
    { nom: "Bob", age: 22, note: 17 },
    { nom: "Charlie", age: 19, note: 15 },
    { nom: "Diane", age: 21, note: 18 }
];

let meilleureNote = etudiants[0].note;
let etudiantMeilleureNote = etudiants[0].nom;
for (let i = 1; i < etudiants.length; i++) {
    if (etudiants[i].note > meilleureNote) {
        meilleureNote = etudiants[i].note;
        etudiantMeilleureNote = etudiants[i].nom;
    }
}
console.log(etudiantMeilleureNote);

for (let i = 0; i < etudiants.length; i++) {
    if (etudiants[i].note >= 15) {
        console.log(etudiants[i].nom);
    }
}

let sommeNotes = 0;
for (let i = 0; i < etudiants.length; i++) {
    sommeNotes += etudiants[i].note;
}
let moyenneClasse = sommeNotes / etudiants.length;
console.log(moyenneClasse);