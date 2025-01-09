const tableau = [5, 12, 67, 98, 14, 99, 1, 210, 67, 40, 8]
let somme = 0

for (let i = 0; i < tableau.length; i++) {
    somme += tableau[i]
}

console.log(somme/tableau.length)