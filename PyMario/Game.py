import pygame
import sys
import json


class Game:
    def __init__(self):
        with open('PyMario/settings.json', 'r') as f:
            settings = json.load(f)
        self.screen = pygame.display.set_mode((settings['WIDTH'], settings['HEIGHT']))
        self.bg_color = (255, 255, 255)

    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def run(self):
        while True:
            self.update_events()
            self.update_screen()

