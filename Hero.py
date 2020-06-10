from Character import Character


class Player(Character):

    def __init__(self, location_w, location_h, movement_rate_w, movement_rate_h, img, size_w, size_h):
        super().__init__(location_w, location_h, movement_rate_w, movement_rate_h, img, size_w, size_h)
        self.can_shot = True
        self.is_moving = False

    def try_to_shot(self, bullets):  # can shot 5 bullets max.
        if self.can_shot is True and len(bullets) < 5:
            return True
