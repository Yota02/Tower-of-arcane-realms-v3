import pygame 
import pytmx 

import pyscroll
from map import MapManager
from player import Player
from song import Songmanager
from item import Item
from inventaire import Inventory
import json

class Game: 

    def __init__(self):
    # Initialisation de la fenêtre Pygame
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h ))
        pygame.display.set_caption("Tower of the Arcane Realms")
        
        self.sound_manager = Songmanager()
        inventory = Inventory()
        
        self.is_playing = True
        self.background = 1
        self.pressed = {}

        self.player = Player()
        
        self.mapmanager = MapManager(self.screen, self.player)
        

    def handle_input(self):
    # Gestion des entrées clavier
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('right')
        elif pressed[pygame.K_DOWN]:
            self.player.change_animation('down')
            self.player.move_down()
        elif pressed[pygame.K_UP]:
            self.player.change_animation('up')
            self.player.move_up()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('left')

    def update(self):
        self.mapmanager.update() 
        
        
    def run(self):
    
        clock = pygame.time.Clock()
        running = True 
        while running:
        
            self.player.save_location()
            self.handle_input()
            self.update()
           
            self.mapmanager.draw()
            
            
            pygame.display.flip()

        
            if self.background == 0:
                self.sound_manager.play('Hub')            

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                      

            clock.tick(60)
