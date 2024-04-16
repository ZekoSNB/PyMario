import sys
import json
from os import environ
from PyMario.Keyboard import Keyboard
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from PyMario.Player import Player


class Game:  # This class is responsible for the game loop and the game window
    def __init__(self): # This method is responsible for initializing the game window (Constructor)
        with open('PyMario/settings.json', 'r') as f:
            settings = json.load(f)
        self.screen = pygame.display.set_mode((settings['WIDTH'], settings['HEIGHT']))
        pygame.init()
        img = pygame.image.load('assets/image/icon.png')
        pygame.display.set_icon(img)
        pygame.display.set_caption(settings['TITLE'])
        self.bg_color = (255, 255, 255)
        self.delta_time = 0
        self.player = Player(0, 0, 50, 50)
        self.clock = pygame.time.Clock()All I want to say is thank you, Danke :). In all honesty it was a wonderful experience to travel abroad alone and to have beautiful memories with you and kamile roaming the city. I don’t know if you did it on purpose, but you have achieved making my trip really fun and pleasant. Currently I’m sitting in the airplane happy to see my girlfriend tomorrow, but I’ll still mention you and Kamile the most since I spent the most time with you. Beautiful time, thank you very much, hopefully the shark is doing fine :)
        self.keyboard = Keyboard()
        self.FPS = settings['FPS']

    def update_events(self):  # This method is responsible for updating the events
        pressed_keys = pygame.key.get_pressed()
        self.player.set_direction(self.keyboard.get_player_dir(self.player, pressed_keys))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def update_screen(self):  # This method is responsible for updating the screen
        self.screen.fill(self.bg_color)
        self.player.update(self.screen)

    def run(self):  # This method is responsible for running the game loop
        while True:
            self.update_events()
            self.delta_time = self.clock.tick(self.FPS) / 1000.0
            self.player.update_physics(self.delta_time)
            self.update_screen()
            pygame.display.flip()
            self.clock.tick(self.FPS)
