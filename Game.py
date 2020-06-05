import Utils
from Bullet import Bullet


class Game:

    def __init__(self, pygame, title, background_img, width, height, icon_url, player, enemies, locations):
        self.pygame = pygame
        self.title = title
        self.pygame.display.set_caption(self.title)
        self.background_img = self.pygame.image.load(background_img)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))  # creating the screen.
        self.display = pygame.display
        self.icon = icon_url
        self.pygame.display.set_icon(self.pygame.image.load(self.icon))
        self.player = player
        self.enemies = enemies
        self.enemy_locations = locations
        self.bullets = []

    def is_legal(self, x, y):
        return self.check_if_in_border(x, y)

    def check_if_in_border(self, x, y):
        return 0 < y < self.height and 0 < x < self.width

    def draw_player(self, x, y):
        if self.is_legal(x, y):
            self.player.loc_w = x
            self.player.loc_h = y
        self.screen.blit(self.player.playerImg, (self.player.loc_w, self.player.loc_h))

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.move(self.enemy_locations)
            self.screen.blit(enemy.img, (enemy.loc_w, enemy.loc_h))

    def draw_bullets(self):
        index_to_remove = []
        for i in range(0, len(self.bullets)):
            if self.bullets[i].loc_h - self.bullets[i].movement_rate > 0:
                self.bullets[i].loc_h -= self.bullets[i].movement_rate
                self.screen.blit(self.bullets[i].bullet_img, (self.bullets[i].loc_w, self.bullets[i].loc_h))
            else:
                index_to_remove.append(i)
        for index in index_to_remove:
            self.bullets.pop(index)

    def bullet_hit(self):
        bullet_to_remove = []
        enemies_to_remove = []
        for i in range(0, len(self.bullets)):
            for j in range(0, len(self.enemies)):
                if Utils.is_collision(self.bullets[i], self.enemies[j]):
                    bullet_to_remove.append(i)
                    enemies_to_remove.append(j)
        for i in bullet_to_remove:
            self.bullets.pop(i)

        for j in enemies_to_remove:
            self.enemies.pop(j)

    def run_loop(self):
        # RGB - Red, Green, Blue
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.background_img, (0, 0))

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
                elif event.key == self.pygame.K_SPACE:
                    if self.player.try_to_shot(self.enemy_locations) is True:
                        self.bullets.append(Bullet(self.pygame, self.player.loc_w, self.player.loc_h, 37, 0.5))

            if event.type == self.pygame.KEYUP:
                if event.key == self.pygame.K_LEFT or event.key == self.pygame.K_RIGHT:
                    self.player.location_change_w = 0
                if event.key == self.pygame.K_UP or event.key == self.pygame.K_DOWN:
                    self.player.location_change_h = 0

        if self.is_legal(self.player.loc_w + self.player.location_change_w,
                         self.player.loc_h + self.player.location_change_h):
            self.player.loc_w += self.player.location_change_w
            self.player.loc_h += self.player.location_change_h

        self.draw_player(self.player.loc_w, self.player.loc_h)
        self.draw_enemies()
        self.draw_bullets()
        self.bullet_hit()
        self.display.update()
        return False  # not quit the game
