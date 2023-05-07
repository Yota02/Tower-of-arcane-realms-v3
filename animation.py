import pygame  

# une classe qui permet d'animer un sprite
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name) :
        super().__init__()
        self.image = self.get_image(0, 0)  # initialiser l'image du sprite à la première image de l'animation
        self.sprite_sheet = pygame.image.load('sprites/player.png')  # charger la feuille de sprite qui contient toutes les images
        self.animation_index  = 0  # initialiser l'index d'animation à 0
        self.images = {
            'down' : self.get_image(17, 142),  # récupérer l'image du sprite orienté vers le bas
            'left' : self.get_image(17, 205),  # récupérer l'image du sprite orienté vers la gauche
            'right' : self.get_image(17, 77),  # récupérer l'image du sprite orienté vers la droite
            'up' : self.get_images(17, 14)  # récupérer l'animation du sprite orienté vers le haut
        }

    # méthode pour changer l'animation du sprite
    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]  # changer l'image du sprite à l'image correspondant à l'index d'animation
        self.image.set_colorkey([0, 0, 0])  # définir la couleur noire comme transparente
        self.animation_index += 1  # augmenter l'index d'animation

    # méthode pour récupérer les images d'une animation
    def get_images(self, y):
        images = []
        for i in range(0, 3):
            x = i *32
            image = self.get_image(x, y)
            images.append(image)
        return images

    # méthode pour récupérer une image à partir de la feuille de sprite
    def get_image(self, x, y):
        image = pygame.Surface([30,48])
        image.blit(self.sprite_sheet, (0, 0), (x, y , 30,48))
        return image
