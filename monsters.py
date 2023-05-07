import pygame  


class Monster(pygame.sprite.Sprite):  # définir une classe Monster qui hérite de la classe Sprite de pygame
    
    def __init__(self, health, attack, speed, resistance, porté, image):
        super().__init__()  # initialiser la classe Sprite parente
        self.health = health  # attribuer les points de vie du monstre
        self.attack = attack  # attribuer la force d'attaque du monstre
        self.speed = speed  # attribuer la vitesse de déplacement du monstre
        self.resistance = resistance  # attribuer la résistance du monstre
        self.porté = porté  # attribuer la portée d'attaque du monstre
        self.image = pygame.image.load(image)  # charger l'image du monstre
        self.image.rect = self.image.get_rect()  # obtenir le rectangle englobant de l'image

# création de monstres

# 1er étage
sanglier = Monster(200, 10, 3, 10, 1, None )  # créer un sanglier avec des attributs spécifiques
loup = Monster(150, 20, 2, 5, 1, None)  # créer un loup avec des attributs spécifiques
squelette = Monster(100, 15, 1, 15, 7, None )  # créer un squelette avec des attributs spécifiques

# Boss du 1er étage
loup_alpha = Monster(500, 30, 1, 15, 3, None )  # créer un loup alpha (boss) avec des attributs spécifiques
  