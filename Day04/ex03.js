mes_nombres = "10,20,30,40"
tableau_nombres = mes_nombres.split(",").map(Number);
console.log(tableau_nombres.length);
somme = 0
for (let i = 0; i < tableau_nombres.length; i++) {
    somme = somme + tableau_nombres[i]
}
console.log(`Somme : ${somme}`);
console.log(`Moyenne : ${somme/tableau_nombres.length}`);

nb_sup_25 = 0
for (let i = 0; i < tableau_nombres.length; i++) {
    if (tableau_nombres[i] >= 25) {
    nb_sup_25++}
}
console.log(`Nombre d’éléments supérieurs à la moyenne : ${nb_sup_25}`)