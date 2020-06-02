
class Player:

    def __init__(self, pygame, player_img, location_x, location_y, movement_rate, location_change_x, location_change_y):
        self.pygame = pygame
        self.playerImg = self.pygame.image.load(player_img)
        self.location_x = location_x
        self.location_y = location_y
        self.movementRate = movement_rate
        self.location_change_x = location_change_x
        self.location_change_y = location_change_y
