import pygame
# controller.py
class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_input(self, events):
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.model.game_manager.is_running = False

        # Oyuncu hareketi
        if not self.model.game_manager.is_paused:
            self.model.player.move(keys)

    def update(self):
        # Düşman hareketi
        for enemy in self.model.enemies:
            enemy.move(self.model.player)

        # Çarpışma kontrolü
        for coin in self.model.coins[:]:
            if coin.check_collision(self.model.player):
                self.model.game_manager.update_score(10)
                self.model.coins.remove(coin)

        # Oyun bitiş kontrolü
        for enemy in self.model.enemies:
            if pygame.Rect(enemy.x, enemy.y, 30, 30).colliderect(self.model.player.x, self.model.player.y, 30, 30):
                self.model.game_manager.end_game(False)
                self.model.game_manager.is_running = False

    def toggle_pause(self):
        self.model.game_manager.toggle_pause()
