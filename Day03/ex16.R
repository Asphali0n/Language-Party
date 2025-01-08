Produit <- c("Pomme", "Orange", "Banane", "Raisin")
Quantite <- c(50, 30, 20, 15)
PrixUnitaire <- c(1.2, 0.8, 0.5, 2.0)

ventes <- data.frame(Produit, Quantite, PrixUnitaire)

ventes$Total <- c(ventes$PrixUnitaire * ventes$Quantite)

print(ventes$Total)

prix_total <- 0
for (i in ventes$Total) {
  prix_total = prix_total + i
}

print(prix_total)
