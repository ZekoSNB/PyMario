from abc import ABC, abstractmethod
from enum import Flag, auto

class CanvasObject(ABC):
    class Direction(Flag):
        STATIC = auto()
        LEFT = auto()
        RIGHT = auto()
        UP = auto()
        DOWN = auto()

    def __init__(self, x, y, width, height, direction=Direction.STATIC):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dir = direction

    @abstractmethod
    def draw_rect(self, screen):
        pass

    @abstractmethod
    def update(self, screen):
        pass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_Direction(self, direction):
        self.dir = direction

