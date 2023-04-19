import pygame 
import animation

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y ) :
        super().__init__()
        self.sprite_sheet = pygame.image.load('sprites/player.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.vie = 100
        self.speed = 3
        self.images = {
            'down' : self.get_image(0, 0),
            'left' : self.get_image(0, 120), 
            'right' : self.get_image(0, 240), 
            'up' : self.get_image(0, 360)
        }


    def change_animation(self, name):
        self.image = self.image[name]
        self.image.set_colorkey([0, 0, 0])

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
    
    def get_image(self, x, y):
        image = pygame.Surface([60, 120])
        image.blit(self.sprite_sheet, (0, 0), (x, y , 60, 120))

        return image