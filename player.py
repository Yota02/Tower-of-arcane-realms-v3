import pygame 
import animation
import json

# Création d'une classe Player qui hérite de pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y ) :
        super().__init__()

        # Chargement de l'image du joueur depuis un fichier
        super().__init__()
        try:
            self.sprite_sheet = pygame.image.load('sprites/player.png')
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image du joueur : {e}")

        self.image = self.get_image(0, 0) # Récupération de la première image du joueur (orienté vers le bas)
        self.image.set_colorkey([0, 0, 0]) # Définition de la couleur à considérer comme transparente sur l'image

        self.rect = self.image.get_rect() # Récupération des dimensions du joueur et de sa position
        self.position = [x, y]

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12) # Définition des dimensions des pieds du joueur et de leur position
        self.old_position = self.position.copy() # Sauvegarde de la position initiale du joueur

        self.images = { # Création d'un dictionnaire contenant les différentes images du joueur selon sa direction
            'down' : self.get_image(17, 142),  # récupérer l'image du sprite orienté vers le bas
            'left' : self.get_image(17, 206),  # récupérer l'image du sprite orienté vers la gauche
            'right' : self.get_image(17, 78),  # récupérer l'image du sprite orienté vers la droite
            'up' : self.get_image(17, 14)  # récupérer l'animation du sprite orienté vers le haut
        }

        # Définition des caractéristiques de base du joueur
        self.speed = 3
        self.lvl = 0
        self.hp = 0 
        self.attack = 1
        self.resistance = 0 
        self.mp = 100
        self.skill = []
        self.inventaire = []
        
    def save_location(self):
        self.old_position = self.position.copy() # Sauvegarde de la position actuelle du joueur

    def change_animation(self, name):
        # Changement de l'image du joueur selon sa direction
        self.image = self.images[name]
        self.image.set_colorkey([0, 0, 0])

    def move_right(self):
        # Déplacement du joueur vers la droite
        self.position[0] += self.speed
    
    def move_left(self):
        # Déplacement du joueur vers la gauche
        self.position[0] -= self.speed

    def move_up(self):
        # Déplacement du joueur vers le haut
        self.position[1] -= self.speed

    def move_down(self):
        # Déplacement du joueur vers le bas
        self.position[1] += self.speed

    def update(self ):
        # Mise à jour de la position et des pieds du joueur
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    def move_back(self):
        # Retour du joueur à sa position précédente
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
    
    def get_image(self, x, y):
        # Récupérer une image à partir de la feuille de sprites
        image = pygame.Surface([30,48])
        image.blit(self.sprite_sheet, (0, 0), (x, y , 30,48))

        return image
    
    """    
    def caracteristique(self):
    # Enregistrer les caractéristiques du joueur dans un fichier JSON
        try:
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
        except FileNotFoundError:
            print("Le fichier n'a pas été trouvé.")
        except IOError:
            print("Erreur d'entrée/sortie.")
        else:
            file.close()
            print("Les caractéristiques ont été enregistrées avec succès.")"""