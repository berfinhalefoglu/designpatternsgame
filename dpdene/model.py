# model.py
from gameManager import GameManager

class GameModel:
    def __init__(self):
        self.game_manager = GameManager()
        self.player = None
        self.enemies = []
        self.coins = []
        self.maze = None

    def initialize(self, maze, player, enemies, coins):
        self.maze = maze
        self.player = player
        self.enemies = enemies
        self.coins = coins
