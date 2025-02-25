# coin.py
import pygame

class Coin:
    def __init__(self, x, y, size=30):
        self.x = x
        self.y = y
        self.size = size

    def check_collision(self, player):
        """Oyuncu ile Coin'in çarpışmasını kontrol et"""
        return pygame.Rect(self.x, self.y, self.size, self.size).colliderect(
            pygame.Rect(player.x, player.y, player.size, player.size)
        )

    def draw(self, screen):
        """Coin'i ekranda çizer."""
        pygame.draw.circle(
            screen, (255, 255, 0), (self.x + self.size // 2, self.y + self.size // 2), self.size // 2
        )  # Sarı renk ile çizer