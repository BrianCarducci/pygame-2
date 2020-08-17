import pygame

class Entity:
    def __init__(self, sprite, x_loc, y_loc, vel):
        self.sprite = sprite
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.vel = vel
