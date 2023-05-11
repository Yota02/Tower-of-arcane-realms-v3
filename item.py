class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage, durability):
        super().__init__(name, description)
        self.damage = damage
        self.durability = durability

class Potion(Item):
    def __init__(self, name, description, effet):
        super().__init__(name, description)
        self.effet = effet

epee_acier = Weapon("Épée en acier", "Une épée forgée en acier", 10, 500)
epee_dragon = Weapon("Épée du dragon", "Une épée légendaire forgée dans le feu des dragon", 15, 2000)
epee_des_ombre = Weapon("Épée des ombre", "Une épée noire forgée dans les ténèbres", 18, 1200)

marteau_guerre = Weapon("Marteau de guerre", "Un marteau de guerre en métal lourd", 15, 700)
marteau_nain = Weapon("Marteau de guerre nain", "Un marteau massif utilisé par les nains", 14, 800)

hache_guerre = Weapon("Hache de guerre", "Une hache lourde utilisée pour fendre les armures", 12, 750)

arc_elfique = Weapon("Arc elfique", "Un arc léger et rapide utilisé par les elfes", 8, 1500)



