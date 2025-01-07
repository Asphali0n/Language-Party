from abc import ABC, abstractmethod
class Employe(ABC):
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    @abstractmethod
    def calculer_salaire(self):
        pass

class EmployeMensuel(Employe):
    def __init__(self, nom, salaire_base):
        super().__init__(nom, salaire_base)

    def calculer_salaire(self):
        salaire = self.salaire_base
        return salaire

class EmployeHoraire(Employe):
    def __init__(self, nom, salaire_base, heures_travaillees):
        super().__init__(nom, salaire_base)
        self.heures_travaillees = heures_travaillees

    def calculer_salaire(self):
        salaire = self.salaire_base * self.heures_travaillees
        return salaire

class Entreprise:
    def __init__(self):
        self.liste_employe = []

    def engager(self,employe):
        self.liste_employe.append(employe)

    def licencier(self,employe):
        self.liste_employe.remove(employe)

    def afficher_employes(self):
        for employe in self.liste_employe:
            print(employe.nom)

    def masse_salariale(self):
        masse_salariale = 0
        for employe in self.liste_employe:
            masse_salariale += employe.calculer_salaire()
        return masse_salariale


employe1 = EmployeMensuel("toto", 55)
employe2 = EmployeMensuel("tata", 34)
employe3 = EmployeHoraire("titi", 66, 36)
employe4 = EmployeHoraire("tutu", 12, 99)

mon_entreprise = Entreprise()

print("avant de licencier toto :")
mon_entreprise.engager(employe1)
mon_entreprise.engager(employe2)
mon_entreprise.engager(employe3)
mon_entreprise.engager(employe4)
mon_entreprise.afficher_employes()

print("après avoir licencié toto :")
mon_entreprise.licencier(employe1)
mon_entreprise.afficher_employes()

print("masse salariale :")
print(mon_entreprise.masse_salariale())








