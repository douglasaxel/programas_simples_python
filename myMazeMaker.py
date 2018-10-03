import pygame
import random
import time


WIDTH = 500
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerador de Labirintos")
clock = pygame.time.Clock()

x = 0
y = 0
w = 20
grid = []
visited = []
stack = []
solution = {}


def build_grid(x, y, w):
    for i in range(1, 21):
        x = 20
        y += 20
        for j in range(1, 21):
            # top
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])
            # rigth
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])
            # bottom
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])
            # left
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])
            grid.append((x, y))
            x += 20
            pygame.display.update()


def push_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39), 0)
    pygame.display.update()


def push_dow(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 19, 39), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w + 1, y + 1, 39, 19), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 39, 19), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()


def solution_line(x, y, x2, y2):
    pygame.draw.line(screen, RED, (x + 10, y + 10), (x2 + 10, y2 + 10))
    pygame.display.update()


def carve_out_maze(x, y):
    single_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        # time.sleep(.07)
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append('rigth')

        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append('left')

        if (x, y + w) not in visited and (x, y + w) in grid:
            cell.append('down')

        if (x, y - w) not in visited and (x, y - w) in grid:
            cell.append('up')

        if len(cell) > 0:
            cell_chosen = random.choice(cell)

            if cell_chosen == 'rigth':
                push_right(x, y)
                solution[(x + w, y)] = x, y
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            if cell_chosen == 'left':
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            if cell_chosen == 'down':
                push_dow(x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            if cell_chosen == 'up':
                push_up(x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))

        else:
            x, y = stack.pop()
            single_cell(x, y)
            # time.sleep(.05)
            backtracking_cell(x, y)


def plot_route_back(x, y):
    while (x, y) != (20, 20):
        x2, y2 = solution[x, y]
        solution_line(x, y, x2, y2)
        time.sleep(.1)


x, y = 20, 20
build_grid(40, 0, 20)
carve_out_maze(x, y)
plot_route_back(400, 400)

exit = True
while exit:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
