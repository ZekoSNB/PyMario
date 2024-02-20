from abc import ABC

import pygame
from PyMario.CanvasObj import CanvasObject


class Player(CanvasObject, ABC):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 60
        self.kinetic_energy = 0

    def draw_rect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def update(self, screen):
        self.draw_rect(screen)

    def move(self, dt):
        if self.dir == self.Direction.LEFT:
            self.x -= self.speed * dt
        if self.dir == self.Direction.RIGHT:
            self.x += self.speed * dt
