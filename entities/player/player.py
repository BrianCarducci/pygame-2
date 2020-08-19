import pygame

from entities.entity import Entity

class Player(pygame.sprite.Sprite):
    collision_side = ""
    colliding_entity = None
    collisions = []


    def __init__(self, image, x_loc, y_loc, vel, is_jumping, jump_count, is_falling):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel
        self.is_jumping = is_jumping
        self.jump_count = jump_count
        self.is_falling = is_falling

    def check_player_action(self, keys):
        if self.is_falling:
            self.rect.y += self.vel
        if self.collisions:
            self.is_falling = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
            # self.x_loc -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
            # self.x_loc += self.vel
        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
            # self.y_loc -= self.vel
        if keys[pygame.K_DOWN]:
            self.rect.y += self.vel
            # self.y_loc += self.vel
        # if keys[pygame.K_SPACE]:
        #     if not self.is_jumping:
        #         self.jump_count -= 1
        #         if self.jump_count <= 

    def check_collision(self, sprite):
        self.collisions = []
        if self.rect.colliderect(sprite.rect):
            if self.rect.bottom <= sprite.rect.top + self.jump_count:
                self.collision_side = "bottom"
            elif self.rect.right > sprite.rect.right:
                self.collision_side = "left"
            elif self.rect.left - self.vel < sprite.rect.left:
                self.collision_side = "right"
            self.collisions.append(
                {
                    "collision_side": self.collision_side,
                    "colliding_entity": type(sprite)
                }
            )
        
