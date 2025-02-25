# game_object.py
import pygame

class GameObject:
    def __init__(self, x, y, speed, color, maze, size=30):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.maze = maze
        self.size = size

    def is_collision(self, new_x, new_y):
        cell_size = self.maze.cell_size
        grid_x = int(new_x // cell_size)
        grid_y = int(new_y // cell_size)

        # Sınır kontrolü
        if grid_y < 0 or grid_y >= len(self.maze.grid) or grid_x < 0 or grid_x >= len(self.maze.grid[0]):
            return True

        # Duvar kontrolü
        return self.maze.grid[grid_y][grid_x] == 1


    def move(self, dx, dy):
        """Labirent çerçevesinde hareket eder."""
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        if not self.is_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        """Objeyi ekranda çizer."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
