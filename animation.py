import pygame 

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name) :
        super().__init__()
        self.image = self.get_image(0, 0)
        self.sprite_sheet = pygame.image.load('sprites/player.png')
        self.animation_index  = 0 
        self.images = {
            'down' : self.get_image(17, 142),
            'left' : self.get_image(17, 205), 
            'right' : self.get_image(17, 77), 
            'up' : self.get_images(17, 14)
        }


    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey([0, 0, 0])
        self.animation_index += 1

    def get_images(self, y):
        images = []
        for i in range(0, 3):
            x = i *32
            image = self.get_image(x, y)
            images.append(image)
        return images

    def get_image(self, x, y):
        image = pygame.Surface([30,48])
        image.blit(self.sprite_sheet, (0, 0), (x, y , 30,48))
        return image