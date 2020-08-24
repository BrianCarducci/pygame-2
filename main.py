import os
import pygame
import pyautogui

from levels.level1 import setup


def main():
    pygame.init()

    # os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(20)

    WINDOW_WIDTH, WINDOW_HEIGHT = pyautogui.size()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

    pygame.display.set_caption("My Game")
    pygame.init()

    player, environment = setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    # sprite_groups = [environment]

    run = True
    while run:
        pygame.time.delay(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # if event.type == pygame.KEYDOWN:

        draw(window, player, environment)

    pygame.quit()


def draw(window, player, sprite_group):
    window.fill((0, 0, 0))
    player.update(window, pygame.key.get_pressed(), sprite_group)
    pygame.display.update()


if __name__ == "__main__":
    main()

