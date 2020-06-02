class Game:

    def __init__(self, pygame, title, width, height, icon_url, player):
        self.pygame = pygame
        self.title = title
        self.pygame.display.set_caption(self.title)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))  # creating the screen.
        self.display = pygame.display
        self.icon = icon_url
        self.pygame.display.set_icon(self.pygame.image.load(self.icon))
        self.player = player

    def check_if_in_border(self, x, y):
        return 0 < y < self.height and 0 < x < self.width

    def draw_player(self, x, y):
        if self.check_if_in_border(x, y):
            self.player.location_x = x
            self.player.location_y = y
            self.screen.blit(self.player.playerImg, (self.player.location_x, self.player.location_y))

    def run_loop(self):
        # RGB - Red, Green, Blue
        self.screen.fill((0, 0, 0))

        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                return True

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_LEFT:
                    self.player.location_change_x = - self.player.movementRate
                elif event.key == self.pygame.K_RIGHT:
                    self.player.location_change_x = self.player.movementRate
                elif event.key == self.pygame.K_UP:
                    self.player.location_change_y = - self.player.movementRate
                elif event.key == self.pygame.K_DOWN:
                    self.player.location_change_y = self.player.movementRate

            if event.type == self.pygame.KEYUP:
                if event.key == self.pygame.K_LEFT or event.key == self.pygame.K_RIGHT:
                    self.player.location_change_x = 0
                if event.key == self.pygame.K_UP or event.key == self.pygame.K_DOWN:
                    self.player.location_change_y = 0

        if self.check_if_in_border(self.player.location_x + self.player.location_change_x,
                                   self.player.location_y + self.player.location_change_y):
            self.player.location_x += self.player.location_change_x
            self.player.location_y += self.player.location_change_y

        self.draw_player(self.player.location_x, self.player.location_y)

        self.display.update()

        return False  # not quit the game
