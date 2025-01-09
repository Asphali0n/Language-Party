let tableau = []

for (let i = 0; i < 50; i++) {
    tableau.push(Math.random()*100);
}

somme = 0
for (let i = 0; i < tableau.length; i++) {
    somme = somme + tableau[i]
}

console.log(`Moyenne : ${somme/tableau.length}`);

let min = tableau[0]
let max = tableau[0]
for (let i = 0; i < tableau.length; i++) {
    if (tableau[i] > max) {
        max = tableau[i]
    }
    if (tableau[i] < min) {
        min = tableau[i]
    }
}

console.log(`Maximum : ${max}, Minimum : ${min}`)

nb_pair = 0
for (let i = 0; i < tableau.length; i++) {
    if (tableau[i] % 2 === 0) {
        nb_pair++
    }
}

console.log(`Nombre de nombres pairs : ${nb_pair}`)