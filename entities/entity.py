import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, sprite, x_loc, y_loc, vel):
        super().__init__(self)
        self.sprite = sprite
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel
