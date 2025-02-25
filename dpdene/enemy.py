# enemy.py
import pygame

from gameObject import GameObject

class Enemy(GameObject):
    def __init__(self, x, y, speed=1, color=(255, 0, 0), maze=None):
        super().__init__(x, y, speed, color, maze)

    def move(self, player):
        """Düşman oyuncuya doğru labirent kurallarına uygun hareket eder."""
        dx = 0
        dy = 0
        if self.x < player.x:
            dx = 1
        elif self.x > player.x:
            dx = -1
        if self.y < player.y:
            dy = 1
        elif self.y > player.y:
            dy = -1
        super().move(dx, dy)