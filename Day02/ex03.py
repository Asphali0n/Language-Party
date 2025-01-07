class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece



class Chien(Animal):
    def parler(self):
        return "Wouf"

class Chat(Animal):
    def parler(self):
        return "Miaou"


class Zoo:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def faire_parler_tout_le_monde(self):
        for animal in self.animaux:
            print(animal.parler())

minou = Chat("minou", "chat")
medor = Chien("medor", "chien")

mon_zoo = Zoo()
mon_zoo.ajouter_animal(minou)
mon_zoo.ajouter_animal(medor)
mon_zoo.faire_parler_tout_le_monde()

