class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_details(self):
        return self.marque, self.modele, self.annee, self.kilometrage

    def augmenter_kilometrage(self, n):
        assert self.kilometrage + n >= 0
        self.kilometrage += n

toto = Voiture("Lamborghini", "Aventador", 2006, 500)
print(toto.afficher_details())
toto.augmenter_kilometrage(3)
print(toto.afficher_details())

tata = Voiture("Fiat", "Multipla", 1999, 999)
print(tata.afficher_details())
toto.augmenter_kilometrage(1)
print(tata.afficher_details())

