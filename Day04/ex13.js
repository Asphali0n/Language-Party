function calculer(nombre1, nombre2, operation) {
    if (operation === "+") {
        return nombre1 + nombre2;
    } else if (operation === "-") {
        return nombre1 - nombre2;
    } else if (operation === "*") {
        return nombre1 * nombre2;
    } else if (operation === "/") {
        if (nombre2 === 0) {
            return "Erreur : division par zéro";
        } else {
            return nombre1 / nombre2;
        }
    } else {
        return "Opération inconnue";
    }
}

console.log(calculer(10, 5, "+"));
console.log(calculer(10, 5, "-"));
console.log(calculer(10, 5, "*"));
console.log(calculer(10, 0, "/"));
