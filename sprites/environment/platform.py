import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x_loc, y_loc, vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.vel = vel

    def update(self, window, player_actions, player_vel):
        mover = 0

        if player_actions:
            if "right" in player_actions:
                mover = player_vel * -1
            if "left" in player_actions:
                mover = player_vel

        self.rect.x += mover
        window.blit(self.image, (self.rect.x, self.rect.y))