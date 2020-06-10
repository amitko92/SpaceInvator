from Character import Character
from random import random


class Enemy(Character):
    def __init__(self, location_w, location_h, movement_rate_w, movement_rate_h, enemy_img, size_w, size_h, index):
        super().__init__(location_w, location_h, movement_rate_w, movement_rate_h, enemy_img, size_w, size_h)
        if random() < 0.5:
            self.direction_w = -1
        self.index = index

    def set_H(self):
        self.loc_h = self.pre_loc_h
        self.change_direction_w()

    def change_direction_w(self):
        self.direction_w *= -1
