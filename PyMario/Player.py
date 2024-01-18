from abc import ABC

import pygame
from CanvasObj import CanvasObject


class Player(CanvasObject, ABC):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        pygame.init()
