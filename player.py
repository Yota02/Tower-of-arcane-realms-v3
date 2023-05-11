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

        # Récupération de la première image du joueur (orienté vers le bas)
        self.image = self.get_image(0, 0)

        # Définition de la couleur à considérer comme transparente sur l'image
        self.image.set_colorkey([0, 0, 0])

        # Récupération des dimensions du joueur et de sa position
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
        
    def save_location(self):
        # Sauvegarde de la position actuelle du joueur
        self.old_position = self.position.copy()

    # Déplacement du joueur vers la droite
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

    # Mise à jour de la position du joueur
    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        # Retour du joueur à sa position précédente
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    # Sauvegarde des caractéristiques du joueur
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
