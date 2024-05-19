import pygame
import random

pygame.init()

# Константы
CELL_SIZE = 10
WIDTH, HEIGHT = 800, 600
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Сетка
cells = [[0 for _ in range(COLS)] for _ in range(ROWS)]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

paused = False
drawing = False
clock = pygame.time.Clock()
FPS = 45

# Цыкл
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                WHITE = (0, 0, 0)
                BLACK = (255, 255, 255)
                if not paused:
                    WHITE = (255, 255, 255)
                    BLACK = (0, 0, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not paused and event.pos[0] >= 0 and event.pos[0] < WIDTH and event.pos[1] >= 0 and event.pos[
                1] < HEIGHT:
                x, y = event.pos
                cells[y // CELL_SIZE][x // CELL_SIZE] = 1 - cells[y // CELL_SIZE][x // CELL_SIZE]
            else:
                drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos
            if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
                cells[y // CELL_SIZE][x // CELL_SIZE] = 1

    # Отрисовка
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if cells[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Обновление во время паузы
    if not paused and not drawing:
        next_cells = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                neighborhood = [cells[i + x][j + y] for x in range(-1, 2) for y in range(-1, 2)]
                neighborhood_count = sum(neighborhood) - cells[i][j]

                if cells[i][j] == 1 and (neighborhood_count == 2 or neighborhood_count == 3):
                    next_cells[i][j] = 1
                elif cells[i][j] == 0 and neighborhood_count == 3:
                    next_cells[i][j] = 1
        cells = [row[:] for row in next_cells]
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
