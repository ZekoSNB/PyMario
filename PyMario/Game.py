from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import threading
import pygame
import json
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
        self.CPPS = 320

    @staticmethod
    def exit(stop_event):
        stop_event.set()

    def update_events(self, stop_event):
        while not stop_event.is_set():

            # delta_time = self.clock.tick(self.FPS) / 1000
            # self.player.update_physics(delta_time)
            # print(delta_time)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit(stop_event)

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
            self.clock.tick(self.CPPS)

    def update_screen(self, stop_event):
        while not stop_event.is_set():
            print(f'graphics {self.clock.get_fps()}')
            self.screen.fill(self.bg_color)
            self.player.update(self.screen)
            self.clock.tick(self.FPS)
            pygame.display.flip()

    def run(self):
        stop_event = threading.Event()
        thread_ph = threading.Thread(target=self.update_events, args=(stop_event,))
        thread_gui = threading.Thread(target=self.update_screen, args=(stop_event,))
        thread_ph.start()
        thread_gui.start()

        thread_ph.join()
        thread_gui.join()
