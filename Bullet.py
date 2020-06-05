from Object import Object


class Bullet(Object):

    def __init__(self, pygame, loc_width, loc_height, r, movement_rate):
        super().__init__(loc_width, loc_height, r)
        self.pygame = pygame
        self.bullet_img = self.pygame.image.load('../images/bullet_2.png')
        self.movement_rate = movement_rate
