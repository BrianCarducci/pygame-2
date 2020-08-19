import pygame

from entities.entity import Entity

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x_loc, y_loc, vel, is_jumping, jump_count, is_falling):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel
        self.is_jumping = is_jumping
        self.jump_count = jump_count
        # super().__init__(sprite, x_loc, y_loc, vel)

    def check_player_action(self, keys):
        if keys[pygame.K_LEFT]:
            self.x_loc -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x_loc += self.vel
        if keys[pygame.K_UP]:
            self.y_loc -= self.vel
        if keys[pygame.K_DOWN]:
            self.y_loc += self.vel
        # if keys[pygame.K_SPACE]:
        #     if not self.is_jumping:
        #         self.jump_count -= 1
        #         if self.jump_count <= 

    def check_collision():
        print(self.sprite.get_rect())
