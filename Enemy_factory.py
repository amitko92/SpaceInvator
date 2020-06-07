from Bullet import Bullet
from Enemy import Enemy


class Factory:
    def __init__(self, images, movement_rate, rs):

        self.images = images  # already loaded
        self.rs = rs
        self.movement_rate = movement_rate

    def create_enemy(self, name, w, h, index):
        return Enemy(w, h, self.rs[name], self.movement_rate[name], self.images[name], index)

    def create_bullet(self, name, w, h):
        return Bullet(w, h, self.rs[name], self.movement_rate[name], self.images[name])
