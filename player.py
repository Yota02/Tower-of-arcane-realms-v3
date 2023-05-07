import pygame 
from animation import AnimateSprite
import json

# Initialisation du joueur
def __init__(self, name, x, y):
    # Appel de la méthode __init__() de la classe parente
    super().__init__(name)
    
    # Configuration de l'image, de sa position, des points de contact, et de la position précédente
    self.image = self.get_image(0, 0)
    self.image.set_colorkey([0, 0, 0])
    self.rect = self.image.get_rect()
    self.position = [x, y]
    self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
    self.old_position = self.position.copy()
    
    # Configuration des caractéristiques du joueur
    self.speed = 3
    self.lvl = 0
    self.hp = 0 
    self.attack = 1
    self.resistance = 0 
    self.mp = 100
    self.skill = []
    self.inventaire = []

# Sauvegarde de la position actuelle du joueur
def save_location(self):
    self.old_position = self.position.copy()

# Déplacement du joueur vers la droite
def move_right(self):
    self.position[0] += self.speed

# Déplacement du joueur vers la gauche
def move_left(self):
    self.position[0] -= self.speed

# Déplacement du joueur vers le haut
def move_up(self):
    self.position[1] -= self.speed

# Déplacement du joueur vers le bas
def move_down(self):
    self.position[1] += self.speed

# Mise à jour de la position du joueur
def update(self):
    self.rect.topleft = self.position
    self.feet.midbottom = self.rect.midbottom

# Retour du joueur à sa position précédente
def move_back(self):
    self.position = self.old_position
    self.rect.topleft = self.position
    self.feet.midbottom = self.rect.midbottom

# Sauvegarde des caractéristiques du joueur
def caracteristique(self):
    with open('data_gama/data_character.json', 'w') as file:
        character = {
            'lvl': self.lvl,
            'stat': {
                'hp': self.hp,
                'mp': self.mp,
                'speed': self.speed,
                'attack': self.attack,
                'resistance': self.resistance
            },
            'skill': self.skill,
            'inventaire': self.inventaire                        
        }
        json.dump(character, file)
        file.close()
