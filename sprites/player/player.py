import pygame

from sprites.environment.platform import Platform

class Player(pygame.sprite.Sprite):

    fall_count = 0

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
        player_actions = []

        # Determines whether or not the player is falling
        collisions = self.check_collision(sprite_group)
        if not self.is_jumping and {"collision_side": "bottom", "collided_sprite": Platform} not in collisions:
            self.is_falling = True
        else:
            self.fall_count = 0
            self.is_falling = False
        if self.is_falling:
            self.fall_count -= 1
            self.rect.y -= self.fall_count 

        # 
        if keys[pygame.K_LEFT]:
            if {"collision_side": "left", "collided_sprite": Platform} not in collisions:
                player_actions.append("left")
        if keys[pygame.K_RIGHT]:
            if {"collision_side": "right", "collided_sprite": Platform} not in collisions:
                player_actions.append("right")
            
        # For all things jumping
        if not self.is_jumping and not self.is_falling:
            if keys[pygame.K_SPACE]:                                                                                  
                self.is_jumping = True
        elif not self.is_falling:
            if self.jump_count <= 0:
                self.is_falling = True
                self.is_jumping = False
            if self.is_jumping:
                self.rect.y -= self.jump_count
                self.jump_count -= 1
            else:
                self.jump_count = self.base_jump_count

        # Draw other sprites relative to player, then draws the player itself as well
        sprite_group.update(window, player_actions, self.vel)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self, sprite_group):
        collisions = []

        collision_side = ""

        collided_sprites = pygame.sprite.spritecollide(self, sprite_group, False)

        for collided_sprite in collided_sprites:
            if self.rect.bottom == collided_sprite.rect.top:
                collision_side = "bottom"
                print("player bottom:" + str(self.rect.bottom))
                print("floor top: " + str(collided_sprite.rect.top))
            elif self.rect.right > collided_sprite.rect.right:
                collision_side = "left"
            elif self.rect.left < collided_sprite.rect.left:
                collision_side = "right"
            collisions.append(
                {
                    "collision_side": collision_side,
                    "collided_sprite": type(collided_sprite)
                }
            )

        return collisions
