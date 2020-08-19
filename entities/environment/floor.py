import pygame

from entities.entity import Entity

class Floor(pygame.sprite.Sprite):
    def __init__(self, sprite, x_loc, y_loc, vel):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel