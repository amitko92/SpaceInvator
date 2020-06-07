# from abc import ABC, abstractmethod


class Object:
    def __init__(self, w, h, r, movement_rate_w, movement_rate_h, img):
        self.loc_w = w
        self.loc_h = h
        self.pre_loc_w = 0
        self.pre_loc_h = 0
        self.radius = r
        self.direction_h = 1
        self.direction_w = 1
        self.movement_rate_h = movement_rate_h
        self.movement_rate_w = movement_rate_w
        self.image = img

    def set_W(self):
        self.loc_w = self.pre_loc_w

    def set_H(self):
        self.loc_h = self.pre_loc_h

    def calculate_move_row(self):
        self.pre_loc_h = self.loc_h + self.direction_h * self.movement_rate_h

    def calculate_move_col(self):
        self.pre_loc_w = self.loc_w + self.direction_w * self.movement_rate_w
