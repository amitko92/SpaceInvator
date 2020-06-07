from Object import Object


class Enemy(Object):
    def __init__(self, location_w, location_h, r, movement_rate_w, movement_rate_h, enemy_img, index):
        super().__init__(location_w, location_h, r, movement_rate_w, movement_rate_h, enemy_img)
        self.dir_moving = 0
        self.index = index

    def set_W(self):
        self.loc_w = self.pre_loc_w

    def set_H(self):
        self.loc_h = self.pre_loc_h
        self.dir_moving *= -1

    def calculate_move_row(self):
        self.pre_loc_h = self.loc_h + self.direction_h * self.movement_rate_h

    def calculate_move_col(self):
        self.pre_loc_w = self.loc_w + self.dir_moving * self.movement_rate_w
        self.pre_loc_h = self.loc_h
