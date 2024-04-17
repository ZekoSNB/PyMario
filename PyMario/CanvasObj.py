from abc import ABC, abstractmethod
from enum import Flag, auto


# CanvasObject is an abstract base class (ABC) that represents an object that can be drawn on a canvas.
class CanvasObject(ABC):
    # Direction is an enumeration that represents the possible directions an object can move in.
    class Direction(Flag):
        STATIC = auto()  # Represents no movement.
        LEFT = auto()  # Represents movement to the left.
        RIGHT = auto()  # Represents movement to the right.

    class JumpingState(Flag):
        GROUNDED = auto()
        MOVING = auto()
        JUMPING = auto()
        FALLING = auto()

    # Constructor for CanvasObject class.
    # @param x: The x-coordinate of the object.
    # @param y: The y-coordinate of the object.
    # @param width: The width of the object.
    # @param height: The height of the object.
    # @param direction: The direction of the object's movement. Defaults to STATIC.
    def __init__(self, x, y, width, height, direction=Direction.STATIC, state=JumpingState.GROUNDED):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dir = direction
        self.state = state

    # Abstract method to draw the object as a rectangle on the screen.
    # @param screen: The pygame screen object where the object will be drawn.
    @abstractmethod
    def draw_rect(self, screen):
        pass

    # Abstract method to update the object.
    # @param screen: The pygame screen object where the object will be drawn.
    @abstractmethod
    def update(self, screen):
        pass

    # Getter for the x-coordinate of the object.
    def get_x(self):
        return self.x

    # Getter for the y-coordinate of the object.
    def get_y(self):
        return self.y

    # Getter for the width of the object.
    def get_width(self):
        return self.width

    # Getter for the height of the object.
    def get_height(self):
        return self.height

    # Setter for the x-coordinate of the object.
    def set_x(self, x):
        self.x = x

    # Setter for the y-coordinate of the object.
    def set_y(self, y):
        self.y = y

    # Setter for the width of the object.
    def set_width(self, width):
        self.width = width

    # Setter for the height of the object.
    def set_height(self, height):
        self.height = height

    # Setter for the direction of the object's movement.
    # @param direction: The new direction of the object's movement.
    def set_direction(self, direction: Direction):
        self.dir = direction

    # Getter for the direction of the object's movement.
    def get_direction(self) -> Direction:
        return self.dir

    def set_state(self, state: JumpingState):
        self.state = state

    def get_state(self) -> JumpingState:
        return self.state
