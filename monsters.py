import pygame
from pygame.sprite import _Group

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, health, attack, speed, resistance, porté, image):
        super().__init__()
        self.health = health
        self.attack = attack
        self.speed = speed
        self.resistance = resistance
        self.porté = porté
        self.image = pygame.image.load(image)
        self.image.rect = self.image.get_rect()
        

# création de monstres

# 1er étage
sanglier = Monster(200, 10, 3, 10, 1, None )
loup = Monster(150, 20, 2, 5, 1, None)
squelette = Monster(100, 15, 1, 15, 7, None )

# Boss du 1er étage
loup_alpha = Monster(500, 30, 1, 15, 3, None )        