from random import random
import math


class Enemy:
    def __init__(self, pygame, enemy_img, location_w, location_h, movement_rate, index):
        self.pygame = pygame
        self.img = self.pygame.image.load(enemy_img)
        self.location_w = location_w
        self.location_h = location_h
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

        temp_location = self.location_w + self.dir_moving * self.movement_rate

        if temp_location < 0 or temp_location > 738:
            self.dir_moving *= -1
            flag = False
        else:
            for location in locations:
                if math.sqrt((temp_location - location[0]) ** 2) < 60 and location[2] != self.index:
                    self.dir_moving *= -1
                    flag = False
        if flag:
            locations[self.index] = (temp_location, self.location_h, self.index)
            self.location_w = temp_location
