import pygame  
from game import Game  

# vérifier si ce fichier est exécuté directement (plutôt qu'importé)
if __name__ == '__main__':
    pygame.init()  # initialiser pygame
    game = Game()  # créer une instance de la classe Game
    game.run()  # exécuter la méthode run() de la classe Game pour lancer le jeu
    