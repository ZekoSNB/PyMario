from abc import ABC
import pygame
from PyMario.CanvasObj import CanvasObject


class Player(CanvasObject, ABC): # Player class inherits from CanvasObject and ABC

    # Constructor for Player class
    # @param x: The x-coordinate of the player
    # @param y: The y-coordinate of the player
    # @param width: The width of the player
    # @param height: The height of the player
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 300  # The speed of the player
        self.kinetic_energy = 0  # The kinetic energy of the player

    # Method to draw the player as a rectangle on the screen
    # @param screen: The pygame screen object where the player will be drawn
    def draw_rect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    # Method to update the physics of the player
    # @param delta_time: The time elapsed since the last frame
    def update_physics(self, delta_time):
        self.move(delta_time)  # Call the move method with delta_time as argument

    # Method to update the player
    # @param screen: The pygame screen object where the player will be drawn
    def update(self, screen):
        self.draw_rect(screen)  # Call the draw_rect method with screen as argument

    # Method to move the player
    # @param delta_time: The time elapsed since the last frame
    def move(self, delta_time):
        if self.dir == self.Direction.STATIC:  # If the player is not moving
            return
        if self.dir == self.Direction.LEFT:  # If the player is moving to the left
            self.x -= self.speed * delta_time  # Update the x-coordinate of the player
        if self.dir == self.Direction.RIGHT:  # If the player is moving to the right
            self.x += self.speed * delta_time  # Update the x-coordinate of the player