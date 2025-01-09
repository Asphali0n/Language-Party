let tableau = [5, 12, 67, 98, 14, 99, 1, 210, 67, 40, 8]

for (let i = 0; i < tableau.length; i++) {
    for (let j = 0; j < tableau.length-1; j++) {
        if (tableau[j] > tableau[j + 1]) {
            let temp = tableau[j];
            tableau[j] = tableau[j + 1];
            tableau[j + 1] = temp;
        }

    }
}

console.log(tableau);