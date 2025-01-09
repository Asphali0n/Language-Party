const phrase = "j'ai pas d'idée de phrase"
nb_mots = 1
for (let i = 0; i < phrase.length; i++) {
    if (phrase[i] === " ") {
        nb_mots++
    }
}

console.log(nb_mots)