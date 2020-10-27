from rasp.lib.menus.main_menu import MainMenu
from rasp.res.glob import *
import pygame


def main():
    pygame.display.init()
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    scr_size = (WIDTH, HEIGHT)
    scr_args = (scr_size, pygame.FULLSCREEN) if FULLSCREEN else (scr_size)
    screen = pygame.display.set_mode(*scr_args)

    print(f"T: {type(MainMenu)}")

    run_args = (screen, clock)
    while True:
        if runtime(*run_args):
            break

    pygame.quit()


def runtime(screen, clock):
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 1

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()

    pygame.display.update()
    return 0


if __name__ == "__main__":
    main()
