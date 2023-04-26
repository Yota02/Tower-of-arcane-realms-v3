import pygame 
import pytmx 
from pytmx.util_pygame import load_pygame
import pyscroll
from player import Player
from song import Songmanager
import json

class Game: 

    def __init__(self):
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h ))
        pygame.display.set_caption("Tower of the Arcane Realms")

        tmx_data = load_pygame('carte/test.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        player_position = tmx_data.get_object_by_name("spawn")
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        
        self.sound_manager = Songmanager()

        self.player = Player(player_position.x, player_position.y)
        self.group.add(self.player)

        self.is_playing = True
        self.background = 0
        self.pressed = {}   

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'colision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def handle_input(self):
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
        self.group.update()
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()




    def run(self):

        clock = pygame.time.Clock()

        running = True 

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            if self.background == 0:
                self.sound_manager.play('Hub')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)