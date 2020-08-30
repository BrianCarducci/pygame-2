import pygame
import os

from sprites.environment.platform import Platform
from sprites.enemies.zombie import Zombie
from sprites.player.player import Player

def setup(window_width, window_height):
    sprite_group = pygame.sprite.Group()

    floor_image = pygame.image.load(os.path.join("assets", "sprites", "environment", "floors", "stone_floor.jpg"))
    zombie_image = pygame.image.load(os.path.join("assets", "sprites", "enemies", "zombie.jpg"))

    base_floor_y_loc = window_height - floor_image.get_rect().h
    floor_x_loc = 0
    for i in range(20):
        sprite_group.add(Platform(floor_image, floor_x_loc, base_floor_y_loc, 0))
        if i == 8:
            sprite_group.add(Zombie(zombie_image, floor_x_loc, base_floor_y_loc - zombie_image.get_rect().h, 0))
        if i == 15:
            sprite_group.add(Platform(floor_image, floor_x_loc, base_floor_y_loc - floor_image.get_rect().h, 0))
        if i == 10:
            sprite_group.add(Platform(floor_image, floor_x_loc, base_floor_y_loc - floor_image.get_rect().h * 3, 0))

        floor_x_loc += floor_image.get_rect().w


    

    player_image = pygame.image.load("assets/sprites/player/123.jpg")
    player = Player(player_image, window_width/2, base_floor_y_loc - player_image.get_rect().h, 30, False, 30, 30, False)

    return player, sprite_group