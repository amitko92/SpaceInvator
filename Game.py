class Game:

    def __init__(self, pygame, title, width, height, icon_url, player, enemies, locations):
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
        self.enemies = enemies
        self.locations = locations

    def is_legal(self, x, y):
        return self.check_if_in_border(x, y)

    def check_if_in_border(self, x, y):
        return 0 < y < self.height and 0 < x < self.width

    def draw_player(self, x, y):
        if self.is_legal(x, y):
            self.player.location_w = x
            self.player.location_h = y
        self.screen.blit(self.player.playerImg, (self.player.location_w, self.player.location_h))

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.move(self.locations)
            self.screen.blit(enemy.img, (enemy.location_w, enemy.location_h))

    def run_loop(self):
        # RGB - Red, Green, Blue
        self.screen.fill((0, 0, 0))

        for event in self.pygame.event.get():

            if event.type == self.pygame.QUIT:
                return True

            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_LEFT:
                    self.player.location_change_w = - self.player.movementRate
                elif event.key == self.pygame.K_RIGHT:
                    self.player.location_change_w = self.player.movementRate
                elif event.key == self.pygame.K_UP:
                    self.player.location_change_h = - self.player.movementRate
                elif event.key == self.pygame.K_DOWN:
                    self.player.location_change_h = self.player.movementRate

            if event.type == self.pygame.KEYUP:
                if event.key == self.pygame.K_LEFT or event.key == self.pygame.K_RIGHT:
                    self.player.location_change_w = 0
                if event.key == self.pygame.K_UP or event.key == self.pygame.K_DOWN:
                    self.player.location_change_h = 0

        if self.is_legal(self.player.location_w + self.player.location_change_w,
                         self.player.location_h + self.player.location_change_h):
            self.player.location_w += self.player.location_change_w
            self.player.location_h += self.player.location_change_h

        self.draw_player(self.player.location_w, self.player.location_h)
        self.draw_enemies()
        self.display.update()
        return False  # not quit the game
