from random import random
from Bullet import Bullet
from Enemy import Enemy


class Factory:
    def __init__(self, images, movement_rate_w, movement_rate_h, size_w, size_h):

        self.images = images  # already loaded
        self.size_w = size_w
        self.size_h = size_h
        self.movement_rate_w = movement_rate_w
        self.movement_rate_h = movement_rate_h

    def create_enemy(self, name, w, h, index):
        if random() < 0.5:  # to move left
            dir_moving = -1
        else:  # to move right
            dir_moving = 1
        e = Enemy(w, h, self.movement_rate_w[name], self.movement_rate_h[name], self.images[name], self.size_w[name], self.size_h[name], index)
        e.dir_moving = dir_moving
        return e

    def create_bullet(self, name, w, h):
        return Bullet(w, h, self.movement_rate_w[name], self.movement_rate_h[name], self.images[name], self.size_w[name], self.size_h[name])
