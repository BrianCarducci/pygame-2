import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x_loc, y_loc, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel

    def update(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))