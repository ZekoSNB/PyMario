from abc import ABC

import pygame
from PyMario.CanvasObj import CanvasObject


class Player(CanvasObject, ABC):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 60
        self.kinetic_energy = 0
        self.delta_time = 0

    def draw_rect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def update(self, screen, delta_time):
        self.draw_rect(screen)
        self.delta_time = delta_time
        self.move()

    def move(self):
        if self.dir == self.Direction.LEFT:
            self.x -= self.speed * self.delta_time
        if self.dir == self.Direction.RIGHT:
            self.x += self.speed * self.delta_time


