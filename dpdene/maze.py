# maze.py
import pygame

class Maze:
    def __init__(self):
        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.cell_size = 50  # Hücre boyutu

    def get_screen_dimensions(self):
        """Ekran genişliği ve yüksekliğini döndür."""
        screen_width = len(self.grid[0]) * self.cell_size
        screen_height = len(self.grid) * self.cell_size
        return screen_width, screen_height

    # maze.py
    def draw(self, screen, wall_color, path_color):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                x = col * self.cell_size  # Hücrenin X koordinatı
                y = row * self.cell_size  # Hücrenin Y koordinatı

                if self.grid[row][col] == 1:  # Duvar
                    pygame.draw.rect(screen, wall_color, (x, y, self.cell_size, self.cell_size))
                elif self.grid[row][col] == 0:  # Yol
                    pygame.draw.rect(screen, path_color, (x, y, self.cell_size, self.cell_size))
