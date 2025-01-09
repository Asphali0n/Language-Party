let votes = ["Pomme", "Banane", "Orange", "Pomme", "Raisin", "Banane", "Banane"];
let resultats = {};

for (let i = 0; i < votes.length; i++) {
    let fruit = votes[i];
    if (resultats[fruit]) {
        resultats[fruit]++;
    } else {
        resultats[fruit] = 1;
    }
}

console.log(resultats);

let fruitGagnant = "";
let maxVotes = 0;
for (let fruit in resultats) {
    if (resultats[fruit] > maxVotes) {
        maxVotes = resultats[fruit];
        fruitGagnant = fruit;
    }
}
console.log(fruitGagnant);
