import sys
import json
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from PyMario.Player import Player


class Game:
    def __init__(self):
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
        self.clock = pygame.time.Clock()
        self.FPS = 80

    def update_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and event.key == pygame.K_d or \
                        event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                    self.player.set_Direction(Player.Direction.STATIC)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.set_Direction(Player.Direction.LEFT)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.set_Direction(Player.Direction.RIGHT)

            if event.type == pygame.KEYUP:
                self.player.set_Direction(Player.Direction.STATIC)

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.update(self.screen)

    def run(self):
        while True:
            self.update_events()
            self.update_screen()
            pygame.display.flip()
            self.clock.tick(self.FPS)
