class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def afficher_produit(self):
        return self.nom, self.prix, self.quantite

class Magasin:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def rechercher_produit(self, produit):
        for i in self.produits:
            if i.nom == produit.nom:
                return produit.afficher_produit()

    def afficher_inventaire(self):
        for i in self.produits:
            print(i.nom)

    def vendre_produit(self,produit):
        if produit.quantite > 0:
            produit.quantite -= 1
            return "Vendu"
        else:
            return "Rupture de stock"




mon_magasin = Magasin()
ordi = Produit("Ordi", 2000, 100)
poulet = Produit("Poulet", 10, 100)
pain_au_chocolat = Produit("Pain au chocolat", 5, 100)
chemise = Produit("Chemise", 20, 100)

print(ordi.afficher_produit())

mon_magasin.ajouter_produit(ordi)
mon_magasin.ajouter_produit(poulet)
mon_magasin.ajouter_produit(pain_au_chocolat)
mon_magasin.ajouter_produit(chemise)

mon_magasin.afficher_inventaire()

print(mon_magasin.rechercher_produit(poulet))
print(mon_magasin.vendre_produit(poulet))
print(mon_magasin.rechercher_produit(poulet))

