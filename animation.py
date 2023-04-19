import pygame 

class AnimationSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name) :
        super().__init__()
        self.image = pygame.image.load('sprites/' + sprite_name + '.png')