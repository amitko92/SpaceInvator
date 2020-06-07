from Object import Object


class Player(Object):

    def __init__(self, width, height, r, movement_rate, player_img, location_change_w, location_change_h):
        super().__init__(width, height, r, movement_rate, player_img)

        self.location_change_w = location_change_w
        self.location_change_h = location_change_h
        self.can_shot = True

    def try_to_shot(self, bullets):  # can shot 5 bullets max.
        if self.can_shot is True and len(bullets) < 5:
            return True
