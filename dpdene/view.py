# view.py
import pygame

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

    def draw(self, model):
        # Ekranı temizle
        self.screen.fill((0, 0, 0))

        # Labirenti, oyuncuyu ve diğer nesneleri çiz
        model.maze.draw(self.screen, 40, (0, 0, 255), (255, 255, 255))
        model.player.draw(self.screen)
        for enemy in model.enemies:
            enemy.draw(self.screen)
        for coin in model.coins:
            coin.draw(self.screen)

        # Skoru çiz
        score_text = self.font.render(f"Score: {model.game_manager.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()
