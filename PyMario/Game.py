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
        self.player = Player(0, 0, 50, 50)
        self.clock = pygame.time.Clock()
        self.FPS = 80

    def events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_d] or keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.player.set_direction(Player.Direction.STATIC)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.set_direction(Player.Direction.LEFT)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.set_direction(Player.Direction.RIGHT)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYUP:
                self.player.set_direction(Player.Direction.STATIC)

    def update_events(self, dt):
        self.player.move(dt)
        self.events()

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.update(self.screen)

    def run(self):
        while True:
            dt = self.clock.tick(self.FPS) / 1000
            self.update_events(dt)
            self.update_screen()
            pygame.display.flip()
            self.clock.tick(self.FPS)
