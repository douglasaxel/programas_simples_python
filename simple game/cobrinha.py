import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0,)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (144, 198, 139)

try:
    pygame.init()
except Exception as e:
    raise e

pygame.mouse.set_visible(False)
x = 640
y = 480
tam = 10
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25, bold=True)


def text(msg, color):
    text1 = font.render(msg, True, color)
    screen.blit(text1, [x * 0.5, y * 0.5])


def snake(snakeXY):
    for xy in snakeXY:
        pygame.draw.rect(screen, black, [xy[0], xy[1], tam, tam])
        #pygame.draw.circle(screen, black, [int(pos_x), int(pos_y)], 6, 0)


def apple(x, y):
    pygame.draw.rect(screen, red, [x, y, tam, tam])


def game():
    exit = True
    endGame = False
    pos_x = random.randint(0, x / 10) * 10
    pos_y = random.randint(0, y / 10) * 10
    apple_x = random.randint(0, x / 10) * 10
    apple_y = random.randint(0, y / 10) * 10
    vel_x = 0
    vel_y = 0
    snakeXY = []
    length = 1

    while exit:
        while endGame:
            screen.fill(background)
            text("Keep playing? y / n", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = False
                    endGame = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        game()
                    if event.key == pygame.K_n:
                        exit = False
                        endGame = False
                        break

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and vel_x != tam:
                    vel_y = 0
                    vel_x = -tam
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and vel_x != -tam:
                    vel_y = 0
                    vel_x = tam
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and vel_y != tam:
                    vel_x = 0
                    vel_y = -tam
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and vel_y != -tam:
                    vel_x = 0
                    vel_y = tam
            if event.type == pygame.QUIT:
                exit = False

        screen.fill(background)
        pos_x += vel_x
        pos_y += vel_y
        snakeHead = []
        snakeHead.append(pos_x)
        snakeHead.append(pos_y)
        snakeXY.append(snakeHead)

        if len(snakeXY) > length:
            del snakeXY[0]

            if any(block == snakeHead for block in snakeHead):
                text("Game Over!", black)
                pygame.display.update()

        snake(snakeXY)
        if pos_x == apple_x and pos_y == apple_y:
            apple_x = random.randint(0, x / 10) * 10
            apple_y = random.randint(0, y / 10) * 10
            length += 10

        apple(apple_x, apple_y)
        pygame.display.update()
        relogio.tick(15)

        if pos_x == x - 10 or pos_y == y - 10:
            vel_x, vel_y = 0, 0
            endGame = True
        if pos_x == 0 or pos_y == 0:
            vel_x, vel_y = 0, 0
            endGame = True

        # if pos_x > x:
        #     pos_x = 0
        # elif pos_x < 0:
        #     pos_x = x - tam
        # elif pos_y > y:
        #     pos_y = 0
        # elif pos_y < 0:
        #     pos_y = y - tam


if __name__ == '__main__':
    game()
    pygame.display.quit()
