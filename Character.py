import pygame


class Character:
    def __init__(self, loc_w, loc_h, movement_rate_w, movement_rate_h, image, size_w, size_h):
        self.loc_w = loc_w
        self.loc_h = loc_h
        self.movement_rate_w = movement_rate_w
        self.movement_rate_h = movement_rate_h
        self.image = image
        self.size_w = size_w
        self.size_h = size_h
        self.rect = pygame.Rect(self.loc_w, self.loc_h, self.size_w, self.size_h)
        self.pre_loc_w = 0
        self.pre_loc_h = 0
        self.direction_w = 1
        self.direction_h = 1

    def set_W(self):
        self.loc_w = self.pre_loc_w

    def set_H(self):
        self.loc_h = self.pre_loc_h

    def calculate_move_row(self):
        self.pre_loc_h = self.loc_h + self.direction_h * self.movement_rate_h

    def calculate_move_col(self):
        self.pre_loc_w = self.loc_w + self.direction_w * self.movement_rate_w
