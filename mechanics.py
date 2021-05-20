import pygame
import numpy as np

pygame.init()
W, H = 1000, 1000
FPS = 30
WHITE = (255, 255, 255)
PINK = (128, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
w = 0.01
T = 0
R = 300
x1 = W // 2
y1 = H // 2

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Моделирование небесной механики")
back = pygame.image.load("back.bmp")
back_rect = back.get_rect(center=(W // 2, H // 2))

sc.blit(back, back_rect)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # нарисуем круг - cолнце
    pygame.draw.circle(sc, YELLOW, (x1, y1), 20)

    # вычислим координаты второго тела при равномерном вращении
    x2 = x1 + R * np.sin(w * T)
    y2 = y1 - R * np.cos(w * T)
    T += 1

    # нарисуем второй круг - спутник
    pygame.draw.circle(sc, PINK, (x2, y2), 3)

    pygame.display.flip()

    clock.tick(FPS)
