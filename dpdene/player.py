# player.py
import pygame
from gameObject import GameObject


class Player(GameObject):
    def __init__(self, x, y, speed=2, color=(0, 0, 255), maze=None):
        super().__init__(x, y, speed, color, maze)

    def move(self, keys):
        """Player'ı klavye girişine göre labirent kurallarına göre hareket ettirir."""
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        super().move(dx, dy)