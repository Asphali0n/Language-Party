class Livre:
    def __init__(self, titre, auteur, disponible):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        if self.disponible:
            self.disponible = False
        else:
            return "Le livre n'est pas disponible"

    def rendre(self):
        if not self.disponible:
            self.disponible = True
        else:
            return "Le livre est déjà là"

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        self.livres_empruntes.append(livre)

    def rendre_livre(self, livre):
        self.livres_empruntes.remove(livre)

class Bibliotheque:
    def __init__(self):
        self.liste = []

    def ajouter_livre(self, livre):
        self.liste.append(livre)

    def afficher_livres(self):
        for livre in self.liste:
            print(livre.titre, livre.auteur, livre.disponible)

    def gerer_emprunt(self, utilisateur, livre, action):
        if action == "emprunter":
            utilisateur.emprunter_livre(livre)
            livre.emprunter()
        else:
            utilisateur.rendre_livre(livre)
            livre.rendre()




livre1 = Livre("1984", "George Orwell", True)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", True)
livre3 = Livre("Les Misérables", "Victor Hugo", True)

alice = Utilisateur("Alice")
bob = Utilisateur("Bob")

ma_bibliotheque = Bibliotheque()
ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.ajouter_livre(livre3)

ma_bibliotheque.afficher_livres()
print("/////////////////////////////")
ma_bibliotheque.gerer_emprunt(alice, livre1, "emprunter")
ma_bibliotheque.afficher_livres()
