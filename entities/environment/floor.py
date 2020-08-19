import pygame

from entities.entity import Entity

class Floor(pygame.sprite.Sprite):
    def __init__(self, image, x_loc, y_loc, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel