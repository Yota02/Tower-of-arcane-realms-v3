import pygame 
from animation import AnimateSprite
import json

class Player(AnimateSprite):
    def __init__(self, name,  x, y) :
        super().__init__(name)
        
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet  = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        
        self.speed = 3
        self.lvl = 0
        self.hp = 0 
        self.attack = 1
        self.resistance = 0 
        self.mp = 100
        self.skill = []
        self.inventaire = []


    def save_location(self):
        self.old_position = self.position.copy()

    def move_right(self):
        self.position[0] += self.speed
    
    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def update(self ):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
    
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