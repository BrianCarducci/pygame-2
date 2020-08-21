import pygame

from sprites.environment.platform import Platform

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
        self.vel = vel
        self.is_jumping = is_jumping
        self.jump_count = jump_count
        self.is_falling = is_falling

    def update(self, window, keys):
        # if not self.is_jumping and {"collision_side": "bottom", "colliding_entity": Floor} not in self.collisions:
        #     self.is_falling = True
        # else:
        #     self.is_falling = False
        # if self.is_falling:
        #     self.rect.y += self.vel
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
        window.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self, sprite):
        self.collisions = []
        if self.rect.colliderect(sprite.rect):
            if self.rect.bottom <= sprite.rect.top + self.vel:
                self.collision_side = "bottom"
                print("bottom")
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
        
