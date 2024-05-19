import pygame
import random
import time

# Константы
WIDTH, HEIGHT = 600, 400
pygame.display.set_caption("Джеф безос")
CELL_SIZE = 5
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (0, 0, 0)
SAND_COLOR = (242, 198, 87)
WATER_COLOR = (87, 103, 242)
FIRE_COLOR = (255, 59, 0)
GRAVEL_COLOR = (66, 71, 71)
STEAM_COLOR = (157, 232, 237)
PLANT_COLOR = (0, 255, 0)
SAND = 1
WATER = 2
FIRE = 3
GRAVEL = 4
STEAM = 5
PLANT = 6
EXPLOSION_RADIUS = 5
FIRE_SPEED = 1
GRAVEL_SPEED = 2
fire_particles = []
gravel_particles = []
mode = 1

# Сетка
grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
drawing = False


# Функция взрыва
def explode(x, y):
    for i in range(max(0, x - EXPLOSION_RADIUS), min(GRID_WIDTH, x + EXPLOSION_RADIUS + 1)):
        for j in range(max(0, y - EXPLOSION_RADIUS), min(GRID_HEIGHT, y + EXPLOSION_RADIUS + 1)):
            if grid[i][j] == SAND:
                grid[i][j] = 0
            elif grid[i][j] == WATER:
                if random.random() < 0.5:
                    grid[i][j] = 0
                else:
                    grid[i][j] = STEAM
                    yg = random.randint(0, 1)
                    create_fire_particle(x - yg, y - yg)
            elif grid[i][j] == FIRE:
                continue
            else:
                grid[i][j] = FIRE

    time.sleep(0.2)

    for i in range(max(0, x - EXPLOSION_RADIUS), min(GRID_WIDTH, x + EXPLOSION_RADIUS + 1)):
        for j in range(max(0, y - EXPLOSION_RADIUS), min(GRID_HEIGHT, y + EXPLOSION_RADIUS + 1)):
            if grid[i][j] == FIRE:
                grid[i][j] = 0
                yg = random.randint(0, 1)
                create_fire_particle(x - yg, y - yg)


def simulate_water(x, y):
    if grid[x][y] == WATER:
        if y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
            grid[x][y], grid[x][y + 1] = 0, WATER
        elif x - 1 >= 0 and y + 1 < GRID_HEIGHT and grid[x - 1][y + 1] == 0:
            grid[x][y], grid[x - 1][y + 1] = 0, WATER
        elif x + 1 < GRID_WIDTH and y + 1 < GRID_HEIGHT and grid[x + 1][y + 1] == 0:
            grid[x][y], grid[x + 1][y + 1] = 0, WATER
        else:
            if x - 1 >= 0 and grid[x - 1][y] == 0:
                grid[x][y], grid[x - 1][y] = 0, WATER
            elif x + 1 < GRID_WIDTH and grid[x + 1][y] == 0:
                grid[x][y], grid[x + 1][y] = 0, WATER

        if grid[x][y] == STEAM:
            if y > 0 and grid[x][y - 1] == 0:
                grid[x][y], grid[x][y - 1] = 0, STEAM


def create_fire_particle(x, y):
    fire_particles.append([x, y])


def create_gravel_particle(x, y):
    gravel_particles.append([x, y])


# Цыкл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            mode += 1
            print(mode)
            if mode > 7:
                mode = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    for particle in fire_particles:
        x, y = particle
        if y > 0:
            grid[x][y] = 0
            grid[x][y - 1] = FIRE
            particle[1] -= FIRE_SPEED
        else:
            fire_particles.remove(particle)
        if FIRE_SPEED == 0:
            fire_particles.remove(particle)

    for particle in gravel_particles:
        x, y = particle

        if y > 0:
            grid[x][y] = 0
            grid[x][y - 1] = GRAVEL
            particle[1] -= GRAVEL_SPEED
        else:
            gravel_particles.remove(particle)
        if 0.05 < 0.1:
            gravel_particles.remove(particle)
        if GRAVEL_SPEED == 0:
            gravel_particles.remove(particle)

    if drawing:
        pos = pygame.mouse.get_pos()
        x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            if pygame.mouse.get_pressed()[0]:
                if mode == 1:
                    grid[x][y] = SAND
                if mode == 2:
                    grid[x][y] = WATER
                if mode == 3:
                    create_fire_particle(x, y)
                if mode == 4:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                        explode(x, y)
                        keys = pygame.key.get_pressed()
                if mode == 5:
                    create_gravel_particle(x, y)
                if mode == 6:
                    grid[x][y] = STEAM
                if mode == 7:
                    grid[x][y] = PLANT
                    grid[x + 1][y] = PLANT
                    grid[x - 1][y] = PLANT
                    grid[x][y - 1] = PLANT
                    grid[x][y + 1] = PLANT

    # Симуляция
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT - 1, 0, -1):
            if grid[x][y] == SAND:
                if y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
                    grid[x][y], grid[x][y + 1] = 0, SAND
                elif y + 1 < GRID_HEIGHT and x - 1 >= 0 and grid[x - 1][y + 1] == 0:
                    if x + 1 < GRID_WIDTH and grid[x + 1][y + 1] == 0:
                        if random.randint(0, 1) == 0:
                            grid[x][y], grid[x - 1][y + 1] = 0, SAND
                        else:
                            grid[x][y], grid[x + 1][y + 1] = 0, SAND
                    elif grid[x - 1][y + 1] == 0:
                        grid[x][y], grid[x - 1][y + 1] = 0, SAND
                    elif grid[x + 1][y + 1] == 0:
                        grid[x][y], grid[x + 1][y + 1] = 0, SAND

                elif y + 1 < GRID_HEIGHT and x - 1 >= 0 and grid[x + 1][y + 1] == 0:
                    if x - 1 < GRID_WIDTH and grid[x - 1][y + 1] == 0:
                        if random.randint(0, 1) == 0:
                            grid[x][y], grid[x][y + 1] = 0, SAND
                        else:
                            grid[x][y], grid[x - 1][y + 1] = 0, SAND
                    elif grid[x - 1][y + 1] == 0:
                        grid[x][y], grid[x + 1][y - 1] = 0, SAND
                    elif grid[x + 1][y + 1] == 0:
                        grid[x][y], grid[x + 1][y - 1] = 0, SAND

            if grid[x][y] == WATER and y > 0 and grid[x][y - 1] == PLANT:
                if y - 1 > 0 and grid[x][y - 2] == 0:
                    grid[x][y - 1], grid[x][y - 2] = 0, PLANT

            if grid[x][y] == GRAVEL:
                if y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
                    grid[x][y], grid[x][y + 1] = 0, GRAVEL
                elif y + 1 < GRID_HEIGHT and x - 1 >= 0 and grid[x - 1][y + 1] == 0:
                    if x + 1 < GRID_WIDTH and grid[x + 1][y + 1] == 0:
                        if random.randint(0, 1) == 0:
                            grid[x][y], grid[x - 1][y + 1] = 0, GRAVEL
                        else:
                            grid[x][y], grid[x + 1][y + 1] = 0, GRAVEL
                    elif grid[x - 1][y + 1] == 0:
                        grid[x][y], grid[x - 1][y + 1] = 0, GRAVEL
                    elif grid[x + 1][y + 1] == 0:
                        grid[x][y], grid[x + 1][y + 1] = 0, GRAVEL

                elif y + 1 < GRID_HEIGHT and x - 1 >= 0 and grid[x + 1][y + 1] == 0:
                    if x - 1 < GRID_WIDTH and grid[x - 1][y + 1] == 0:
                        if random.randint(0, 1) == 0:
                            grid[x][y], grid[x][y + 1] = 0, GRAVEL
                        else:
                            grid[x][y], grid[x - 1][y + 1] = 0, GRAVEL
                    elif grid[x - 1][y + 1] == 0:
                        grid[x][y], grid[x + 1][y - 1] = 0, GRAVEL
                    elif grid[x + 1][y + 1] == 0:
                        grid[x][y], grid[x + 1][y - 1] = 0, GRAVEL

            simulate_water(x, y)

            if grid[x][y] == STEAM:
                if random.random() < 0.5:
                    if x + 1 < GRID_WIDTH and grid[x + 1][y] == 0:
                        grid[x][y], grid[x + 1][y] = 0, STEAM
                else:
                    if x - 1 >= 0 and grid[x - 1][y] == 0:
                        grid[x][y], grid[x - 1][y] = 0, STEAM

            if grid[x][y] == SAND and y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
                grid[x][y], grid[x][y + 1] = 0, SAND

            elif grid[x][y] == WATER and y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
                grid[x][y], grid[x][y + 1] = 0, WATER

            elif grid[x][y] == FIRE and y + 1 < GRID_HEIGHT and grid[x][y] == 0:
                grid[x][y], grid[x][y + 1] = 0, FIRE

            elif grid[x][y] == SAND and y + 1 < GRID_HEIGHT and grid[x][y + 1] == WATER:
                grid[x][y], grid[x][y + 1] = WATER, SAND

            elif grid[x][y] == GRAVEL and y + 1 < GRID_HEIGHT and grid[x][y + 1] == WATER:
                grid[x][y], grid[x][y + 1] = WATER, GRAVEL

            elif grid[x][y] == PLANT and y + 1 < GRID_HEIGHT and grid[x][y + 1] == WATER:
                grid[x][y], grid[x][y + 1] = PLANT, PLANT

            elif grid[x][y] == WATER and y + 1 < GRID_HEIGHT and grid[x][y + 1] == PLANT:
                grid[x][y], grid[x][y + 1] = PLANT, PLANT

            elif grid[x][y] == WATER and y + 1 < GRID_HEIGHT and grid[x][y + 1] == FIRE:
                grid[x][y], grid[x][y + 1] = 0, STEAM

            elif grid[x][y] == GRAVEL and y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
                grid[x][y], grid[x][y + 1] = 0, GRAVEL

    # Отрисовка
    screen.fill(WHITE)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == SAND:
                pygame.draw.rect(screen, SAND_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[x][y] == WATER:
                pygame.draw.rect(screen, WATER_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[x][y] == FIRE:
                pygame.draw.rect(screen, FIRE_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[x][y] == GRAVEL:
                pygame.draw.rect(screen, GRAVEL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[x][y] == STEAM:
                pygame.draw.rect(screen, STEAM_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[x][y] == PLANT:
                pygame.draw.rect(screen, PLANT_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(40)
