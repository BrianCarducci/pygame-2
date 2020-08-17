import pygame

from entities.entity import Entity

class Player(Entity):
    def __init__(self, sprite, x_loc, y_loc, vel):
        super().__init__(sprite, x_loc, y_loc, vel)

    def check_player_action(self, keys):
        if keys[pygame.K_LEFT]:
            print("left")
        if keys[pygame.K_RIGHT]:
            self.x_loc += self.vel
        if keys[pygame.K_UP]:
            print("up")
        if keys[pygame.K_DOWN]:
            print("down")
