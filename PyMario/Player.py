from abc import ABC
import pygame
from PyMario.CanvasObj import CanvasObject


class Player(CanvasObject, ABC):  # Player class inherits from CanvasObject and ABC

    # Constructor for Player class
    # @param x: The x-coordinate of the player
    # @param y: The y-coordinate of the player
    # @param width: The width of the player
    # @param height: The height of the player
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.ground_speed = 300  # The speed of the player
        self.ground_height = 500
        self.max_velocity = 500  # The maximum velocity of the player
        self.velocity = 0  # The velocity of the player
        self.kinetic_energy = 0  # The kinetic energy of the player

    # Method to draw the player as a rectangle on the screen
    # @param screen: The pygame screen object where the player will be drawn
    def draw_rect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    # Method to update the physics of the player
    # @param delta_time: The time elapsed since the last frame
    def update_physics(self, delta_time):
        # Kinetic energy equation => E_k = 0.5 * m * v^2

        self.kinetic_energy = 0.5 * 1 * self.velocity ** 2  # Calculate the kinetic energy of the player

        print(self.y)
        player_touching_ground = self.y = self.ground_height
        player_want_to_jump = self.state == self.JumpingState.JUMPING

        if player_touching_ground:
            self.state = self.JumpingState.GROUNDED

        if player_want_to_jump:
            print('jumping')
            self.set_y(self.y + self.velocity * delta_time)
            self.velocity += 2
        elif self.y < self.ground_height and self.velocity >= 0:
            self.set_y(self.y + self.velocity * delta_time)  # Update the y-coordinate of the player
            self.velocity += 250 * delta_time  # Update the velocity of the player

        elif self.y > self.ground_height:
            self.state = self.JumpingState.GROUNDED
            print('falling')
            self.set_y(self.ground_height)
            self.velocity = 0
        self.move(delta_time)  # Call the move method with delta_time as
        self.jump()

    # Method to update the player
    # @param screen: The pygame screen object where the player will be drawn
    def update(self, screen):
        self.draw_rect(screen)  # Call the draw_rect method with screen as argument

    # Method to move the player
    # @param delta_time: The time elapsed since the last frame
    def move(self, delta_time):
        if self.dir == self.Direction.STATIC:  # If the player is not moving
            return
        match self.dir:
            case self.Direction.LEFT:   # If the player is moving to the left
                self.x -= self.ground_speed * delta_time  # Update the x-coordinate of the player
            case self.Direction.RIGHT:  # If the player is moving to the right
                self.x += self.ground_speed * delta_time  # Update the x-coordinate of the player

    def jump(self):
        if self.y == self.ground_height and self.state == self.JumpingState.GROUNDED or \
                self.state == self.JumpingState.MOVING:
            self.velocity = -1000
            self.state = self.JumpingState.JUMPING
