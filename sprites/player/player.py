import pygame

from sprites.environment.platform import Platform

class Player(pygame.sprite.Sprite):

    def __init__(self, image, x_loc, y_loc, vel, is_jumping, base_jump_count, jump_count, is_falling):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.vel = vel
        self.is_jumping = is_jumping
        self.base_jump_count = base_jump_count
        self.jump_count = jump_count
        self.is_falling = is_falling

    def update(self, window, keys, sprite_group):
        collisions = self.check_collision(sprite_group)
        if not self.is_jumping and {"collision_side": "bottom", "collided_sprite": Platform} not in collisions:
            self.is_falling = True
        else:
            self.is_falling = False
        if self.is_falling:
            self.rect.y += self.vel

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        
        if not self.is_jumping and not self.is_falling:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        elif not self.is_falling:
            if self.jump_count <= 0:
                self.is_falling = True
                self.is_jumping = False
                print("huh")
                self.jump_count = self.base_jump_count
            else:
                print("jumping")
                self.jump_count -= 1
                self.rect.y -= 1
               
        window.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self, sprite_group):
        collisions = []

        collision_side = ""

        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, False)

        for collided_sprite in collided_sprites:
            if self.rect.bottom >= collided_sprite.rect.top:
                collision_side = "bottom"

            collisions.append(
                {
                    "collision_side": collision_side,
                    "collided_sprite": type(collided_sprite)
                }
            )

        return collisions
        

                

        # self.collisions = []
        # if self.rect.colliderect(sprite.rect):
        #     if self.rect.bottom <= sprite.rect.top + self.vel:
        #         self.collision_side = "bottom"
        #         print("bottom")
        #     elif self.rect.right > sprite.rect.right:
        #         self.collision_side = "left"
        #     elif self.rect.left - self.vel < sprite.rect.left:
        #         self.collision_side = "right"
        #     self.collisions.append(
        #         {
        #             "collision_side": self.collision_side,
        #             "colliding_entity": type(sprite)
        #         }
        #     )
        
