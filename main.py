from rasp.res.glob import *
from time import time
import pygame


def main():
    pygame.display.init()
    pygame.display.set_caption(TITLE)

    screen_size = (WIDTH, HEIGHT)
    if FULLSCREEN:
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(screen_size)

    while True:
        if runTime(screen):
            break

    pygame.quit()


def runTime(screen):
    startTime = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()

    update(screen, startTime, FPS)
    return 0


def update(screen, startTime, fps):
    # ekrana yazıldı
    pygame.display.update()
    # fps düzenlemesi
    while time() - startTime < (1 / fps):
        pass


if __name__ == "__main__":
    main()
