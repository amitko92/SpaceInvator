import math
from random import random

from Object import Object


class Enemy(Object):
    def __init__(self, location_w, location_h, r, movement_rate, enemy_img, index):
        super().__init__(location_w, location_h, r, movement_rate, enemy_img)
        self.pre_loc_w = 0
        self.pre_loc_h = 0
        self.dir_moving = 0
        self.index = index

    def set_W(self):
        self.loc_w = self.pre_loc_w

    def set_H(self):
        self.loc_h = self.pre_loc_h
        self.dir_moving *= -1

    def calculate_move_row(self):
        self.pre_loc_h = self.loc_h + 70

    def calculate_move_col(self):
        if self.dir_moving == 0:
            if random() < 0.5:  # to move left
                self.dir_moving = -1
            else:  # to move right
                self.dir_moving = 1

        self.pre_loc_w = self.loc_w + self.dir_moving * self.movement_rate
        self.pre_loc_h = self.loc_h
