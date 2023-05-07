import pygame

class Songmanager():
    def __init__(self) :
        # Initialisation d'un dictionnaire pour stocker les sons et leurs noms
        self.sound = {
            'Hub' : pygame.mixer.Sound('song/music/Fountain Of Eternity  Majestic Fantasy Orchestral  Epic Fantasy Adventure Mix - Eternal Eclipse.mp3'),
        }

    def play(self, name):
        # Lecture du son associé au nom donné
        self.sound[name].play()

