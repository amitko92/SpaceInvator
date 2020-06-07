from Object import Object


class Player(Object):

    def __init__(self, width, height, r, movement_rate_w, movement_rate_h, player_img):
        super().__init__(width, height, r, movement_rate_w, movement_rate_h, player_img)
        self.can_shot = True
        self.is_moving = False

    def try_to_shot(self, bullets):  # can shot 5 bullets max.
        if self.can_shot is True and len(bullets) < 5:
            return True
