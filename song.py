import pygame

class Songmanager():

    def __init__(self) :
        self.sound = {
            'Hub' : pygame.mixer.Sound('song/music/Fountain Of Eternity  Majestic Fantasy Orchestral  Epic Fantasy Adventure Mix - Eternal Eclipse.mp3')

        }

    def play(self, name):
        self.sound[name].play()
