library(ggplot2)

Produit <- c("Pomme", "Orange", "Banane", "Raisin")
Quantité <- c(50, 30, 20, 15)
Prix <- c(1.2, 0.8, 0.5, 2.0)

ventes <- data.frame(Produit, Quantité, Prix)

ventes$Total <- c(ventes$Prix * ventes$Quantité)

graphique = ggplot(ventes,aes(x = Produit,y = Quantité))+geom_bar(stat = "identity", fill = c("red", "orange", "yellow", "purple")) + ggtitle("Totaux des ventes par produit") + xlab("Produits") + ylab("Total des ventes (euros)")
print(graphique)