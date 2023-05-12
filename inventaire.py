class Inventory:
    def __init__(self):
        self.capacity = 100  # Capacité maximale de l'inventaire
        self.items = []  # Liste des objets dans l'inventaire
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])

    def ajouter_objet(self, objet):
        if len(self.objets) < self.capacite:  # Vérifier si l'inventaire est plein
            self.objets.append(objet)  # Ajouter l'objet à la liste des objets
            print(f"{objet.nom} a été ajouté à l'inventaire.")  # Afficher un message de confirmation
        else:
            print("L'inventaire est plein.")  # Afficher un message d'erreur si l'inventaire est plein

    def supprimer_objet(self, objet):
        if objet in self.objets:  # Vérifier si l'objet est dans l'inventaire
            self.objets.remove(objet)  # Retirer l'objet de la liste des objets
            print(f"{objet.nom} a été retiré de l'inventaire.")  # Afficher un message de confirmation
        else:
            print(f"{objet.nom} n'est pas dans l'inventaire.")  # Afficher un message d'erreur si l'objet n'est pas dans l'inventaire

    def afficher_inventaire(self):
        print("Inventaire :")  # Afficher le titre de l'inventaire
        if len(self.objets) == 0:
            print("Vide")  # Afficher un message si l'inventaire est vide
        else:
            for objet in self.objets:
                print(f"{objet.nom} - {objet.description}")  # Afficher le nom et la description de chaque objet dans l'inventaire
