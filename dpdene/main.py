import pygame
from gameManager import GameManager
from maze import Maze
from player import Player
from enemy import Enemy
from coin import Coin

def main():
    pygame.init()

    # GameManager'i başlat
    game_manager = GameManager()

    # Maze'i oluştur
    maze = Maze()
    screen_width, screen_height = maze.get_screen_dimensions()

    # Ekranı ayarla
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Lock 'n' Chase - Geniş Labirent")
    clock = pygame.time.Clock()

    # Modelde gerekli nesneler
    player = Player(maze.cell_size, maze.cell_size, maze=maze)  # Başlangıç pozisyonu (1, 1)
    enemies = [
        Enemy(maze.cell_size * 3, maze.cell_size * 2, maze=maze),
        Enemy(maze.cell_size * 7, maze.cell_size * 5, maze=maze),
        Enemy(maze.cell_size * 11, maze.cell_size * 7, maze=maze)
    ]
    coins = [
        Coin(maze.cell_size * 2, maze.cell_size * 2),
        Coin(maze.cell_size * 6, maze.cell_size * 6),
        Coin(maze.cell_size * 10, maze.cell_size * 3)
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        for enemy in enemies:
            enemy.move(player)

        # Coin'lerin toplanmasını kontrol et ve skoru artır
        for coin in coins[:]:
            if coin.check_collision(player):
                coins.remove(coin)
                game_manager.update_score(10)  # Skor 10 puan artırılır
                print(f"Skor: {game_manager.get_score()}")  # Skoru konsola yazdır

        # Ekranı temizle ve nesneleri çiz
        screen.fill((0, 0, 0))
        maze.draw(screen, (0, 0, 255), (255, 255, 255))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for coin in coins:
            coin.draw(screen)

        # Skoru ekranda göster
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {game_manager.get_score()}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
