import os
import pygame
import pyautogui

from entities.player.player import Player


def main():
    pygame.init()

    # os.environ['SDL_VIDEO_WINDOW_POS'] = str(0) + "," + str(20)

    WINDOW_WIDTH, WINDOW_HEIGHT = 2560, 1440
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("My Game")
    pygame.init()

    player_sprite = pygame.image.load("assets/sprites/player/123.jpg")
    player = Player(player_sprite, 10)

    # player = entities[0]
    text_surface = None

    run = True
    while run:
        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # if event.type == pygame.KEYDOWN:
                
        keys = pygame.key.get_pressed()

        draw(window, player)

    pygame.quit()


def draw(window, player):
    window.fill((0, 0, 0))

    window.blit(player.sprite, (50, 50))

    # for entity in entities:
        # win.blit(background, (background_x, 0))
        # win.blit(background, (background_x2, 0))

    # if text_surface:
    #     w, h = pygame.display.get_surface().get_size()
    #     print("from get surface: " + str(win.get_width()) + ", " + str(win.get_height()))
    #     win.blit(text_surface, (window_width//2, window_height//2))

    pygame.display.update()


if __name__ == "__main__":
    main()

