from Character import Character


class Bullet(Character):

    def __init__(self, location_w, location_h, movement_rate_w, movement_rate_h, img, size_w, size_h):
        super().__init__(location_w, location_h, movement_rate_w, movement_rate_h, img, size_w, size_h)
