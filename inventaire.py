class Inventory:
    def __init__(self):
        self.capacity = 100
        self.items = []

    def ajouter_objet(self, objet):
        if len(self.objets) < self.capacite:
            self.objets.append(objet)
            print(f"{objet.nom} a été ajouté à l'inventaire.")
        else:
            print("L'inventaire est plein.")

    def supprimer_objet(self, objet):
        if objet in self.objets:
            self.objets.remove(objet)
            print(f"{objet.nom} a été retiré de l'inventaire.")
        else:
            print(f"{objet.nom} n'est pas dans l'inventaire.")

    def afficher_inventaire(self):
        print("Inventaire :")
        if len(self.objets) == 0:
            print("Vide")
        else:
            for objet in self.objets:
                print(f"{objet.nom} - {objet.description}")



