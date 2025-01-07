import time

class Personnage:
    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def attaquer(self,perso_attaque):
        perso_attaque.points_de_vie -= self.force

class Guerrier(Personnage):
    def __init__(self, nom, points_de_vie, force):
        super().__init__(nom, points_de_vie, force)
        self.force += 10

class Mage(Personnage):
    def attaquer(self,perso_attaque):
        perso_attaque.points_de_vie -= self.force + 5

class Combat:
    def __init__(self, personnage1, personnage2):
        self.personnage1 = personnage1
        self.personnage2 = personnage2

    def lancer_combat(self):
        attaquant = self.personnage1
        attaque = self.personnage2
        while True:
            if attaquant.points_de_vie <= 0:
                print(f"Le combat est fini ! {attaquant.nom} gagne !")
                break
            elif attaque.points_de_vie <= 0:
                print(f"Le combat est fini ! {attaque.nom} gagne !")
                break
            else:
                attaquant.attaquer(attaque)
                print(f"{attaquant.nom} attaque {attaque.nom} !")
                time.sleep(0.5)
                attaquant, attaque = attaque, attaquant

mon_guerrier = Guerrier("toto", 100, 10)
mon_mage = Mage("titi", 100, 10)
mon_combat = Combat(mon_guerrier, mon_mage)
mon_combat.lancer_combat()




