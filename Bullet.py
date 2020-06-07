from Object import Object


class Bullet(Object):

    def __init__(self, loc_width, loc_height, r, movement_rate_w, movement_rate_h, bullet_image):
        super().__init__(loc_width, loc_height, r, movement_rate_w, movement_rate_h, bullet_image)
