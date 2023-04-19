import pygame 
import pytmx 
from pytmx.util_pygame import load_pygame
import pyscroll
from player import Player

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
        
        self.player = Player(player_position.x, player_position.y)
        self.group.add(self.player)

        self.is_playing = True
        self.background = 4
        self.pressed = {}   

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()


    def run(self):

        clock = pygame.time.Clock()

        running = True 

        while running:
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)