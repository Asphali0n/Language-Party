const tableau = [5, 8, 67, 98, 15, 99, 1, 0, 67, 40]
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