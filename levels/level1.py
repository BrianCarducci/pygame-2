import pygame
import os

from sprites.environment.platform import Platform
from sprites.player.player import Player

def setup(window_width, window_height):
    environment_sprite_group = pygame.sprite.Group()

    floor_image = pygame.image.load(os.path.join("assets", "sprites", "environment", "floors", "stone_floor.jpg"))
    base_floor_y_loc = window_height - floor_image.get_rect().h
    floor_x_loc = 0
    for i in range(20):
        environment_sprite_group.add(Platform(floor_image, floor_x_loc, base_floor_y_loc, 0))
        floor_x_loc += floor_image.get_rect().w

    player_image = pygame.image.load("assets/sprites/player/123.jpg")
    player = Player(player_image, window_width/2, 300, 10, False, 10, 10, False)

    return player, environment_sprite_group