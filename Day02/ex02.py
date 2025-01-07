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

    def calculer_age(self):
        annee_actuelle = 2025
        return annee_actuelle - self.annee

    def est_vieille(self):
        if self.calculer_age() > 10:
            return True
        return False


toto = Voiture("Lamborghini", "Aventador", 2006, 500)
print(toto.calculer_age())
print(toto.est_vieille())

tata = Voiture("Fiat", "Multipla", 2023, 999)
print(tata.calculer_age())
print(tata.est_vieille())
