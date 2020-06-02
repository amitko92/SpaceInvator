
class Player:

    def __init__(self, pygame, player_img, width, height, movement_rate, location_change_w, location_change_h):
        self.pygame = pygame
        self.playerImg = self.pygame.image.load(player_img)
        self.location_w = width
        self.location_h = height
        self.movementRate = movement_rate
        self.location_change_w = location_change_w
        self.location_change_h = location_change_h
