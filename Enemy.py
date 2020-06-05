import math
from random import random

from Object import Object


class Enemy(Object):
    def __init__(self, pygame, enemy_img, location_w, location_h, r, movement_rate, index):
        super().__init__(location_w, location_h, r)
        self.pygame = pygame
        self.img = self.pygame.image.load(enemy_img)
        self.loc_w = location_w
        self.loc_h = location_h
        self.movement_rate = movement_rate
        self.dir_moving = 0
        self.index = index

    def move(self, locations):
        temp_location = 0
        flag = True

        if self.dir_moving == 0:
            if random() < 0.5:  # to move left
                self.dir_moving = -1
            else:  # to move right
                self.dir_moving = 1

        temp_location = self.loc_w + self.dir_moving * self.movement_rate

        if temp_location < 0 or temp_location > 738:  # 62
            locations[self.index] = (self.loc_w, self.loc_h + 62, self.index)
            self.loc_h += 70
            self.dir_moving *= -1
            flag = False
        else:
            for location in locations:
                if math.sqrt((temp_location - location[0]) ** 2) < 60 and location[2] != self.index and self.loc_h == \
                        location[1]:
                    self.dir_moving *= -1
                    flag = False
        if flag:
            locations[self.index] = (temp_location, self.loc_h, self.index)
            self.loc_w = temp_location
