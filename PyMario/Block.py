from abc import ABC
from PyMario.CanvasObj import CanvasObject


class Block(CanvasObject, ABC):
    # Constructor for Block class.
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
