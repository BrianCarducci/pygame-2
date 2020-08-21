import pygame
import os

from sprites.environment.platform import Platform
from sprites.player.player import Player

def setup(window_width, window_height):
    environment_sprite_group = pygame.sprite.Group()

    floor_image = pygame.image.load(os.path.join("assets", "sprites", "environment", "floors", "stone_floor.jpg"))
    floor_1 = Platform(floor_image, 0, window_height - floor_image.get_rect().h, 0)
    environment_sprite_group.add(floor_1)

    player_image = pygame.image.load("assets/sprites/player/123.jpg")
    player = Player(player_image, window_width/2, window_height - floor_1.rect.y, 10, False, 10, False)

    return player, environment_sprite_group