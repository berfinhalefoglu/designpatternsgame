# gameManager.py
class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.score = 0  # Başlangıç skoru
            self.initialized = True

    def update_score(self, points):
        """Skoru artırır."""
        self.score += points

    def get_score(self):
        """Skoru döndürür."""
        return self.score

    def start_game(self):
        """Oyunu başlatır."""
        self.score = 0

    def end_game(self, won):
        """Oyunun sonunda sonucu yazdırır."""
        if won:
            print("You won!")
        else:
            print("Game Over")
