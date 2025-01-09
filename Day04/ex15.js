let panier = [
    { nom: "Pomme", prix: 2, quantite: 3 },
    { nom: "Banane", prix: 1, quantite: 5 },
    { nom: "Orange", prix: 3, quantite: 2 }
];

let prixTotal = 0;
for (let i = 0; i < panier.length; i++) {
    prixTotal += panier[i].prix * panier[i].quantite;
}
console.log(prixTotal);

panier.push({ nom: "Fraise", prix: 4, quantite: 1 });

let nomASupprimer = "Banane";
for (let i = 0; i < panier.length; i++) {
    if (panier[i].nom === nomASupprimer) {
        panier.splice(i, 1);
        break;
    }
}

console.log(panier);
