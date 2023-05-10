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

epee_acier = Weapon("Épée en acier", "Une épée forgée en acier", 10, 50)

