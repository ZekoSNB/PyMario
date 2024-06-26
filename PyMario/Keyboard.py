import pygame
from PyMario.Player import Player


class Keyboard:  # Keyboard class is responsible for handling keyboard inputs
    # Static method to get the direction of the player based on keyboard inputs
    # @param player: The player object whose direction is to be determined
    # @return: The direction of the player based on the keyboard inputs
    @staticmethod
    def get_player_dir(player: Player, pressed_keys):
        # Get the state of all keyboard buttons

        # If both left and right keys (A and D or LEFT and RIGHT arrow keys) are pressed, player's direction is static
        if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_d] or \
                pressed_keys[pygame.K_LEFT] and pressed_keys[pygame.K_RIGHT]:
            return player.Direction.STATIC

        # If left key (A or LEFT arrow key) is pressed, player's direction is left
        elif pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            return player.Direction.LEFT

        # If right key (D or RIGHT arrow key) is pressed, player's direction is right
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            return player.Direction.RIGHT

    @staticmethod
    def get_player_jump(player: Player, pressed_keys, state: Player.JumpingState):
        if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_w]) and \
                state == player.JumpingState.GROUNDED or state == player.JumpingState.MOVING:
            return player.JumpingState.JUMPING
