import Utils
import time


class Game:

    def __init__(self, pygame, title, background_img, width, height, icon_url, player, factory):
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
        self.enemies = {}
        self.enemies_counter = 0
        self.bullets = []
        self.score_value = 0
        self.text_w = 10
        self.text_h = 10
        self.score_font = pygame.font.Font('freesansbold.ttf', 32)
        self.enemy_factory = factory

        self.init_enemies()

    def game_over(self, w, h, massage):
        self.end_game_massage += massage
        massage_rander = self.end_game_font.render(self.end_game_massage, True, (250, 250, 250))
        self.screen.blit(massage_rander, (w, h))

    def show_score(self, w, h):
        score = self.score_font.render("Score: " + str(self.score_value), True, (250, 250, 250))
        self.screen.blit(score, (w, h))

    def is_legal(self, x, y):
        return self.check_if_in_border(x, y)

    def check_if_in_border(self, x, y):
        return 0 < y < self.height and 0 < x < self.width

    def move_enemies(self):
        for index in self.enemies:
            flag = False
            self.enemies[index].calculate_move_col()
            if self.enemies[index].pre_loc_w < 0 or self.enemies[index].pre_loc_w > 738:
                self.enemies[index].calculate_move_row()
                self.enemies[index].set_H()  # right now I don't check if move is legal.
            else:
                for other_enemy_index in self.enemies:
                    if not (self.enemies[other_enemy_index].index == self.enemies[index].index):
                        if Utils.is_collision(self.enemies[index], self.enemies[other_enemy_index]):
                            self.enemies[index].dir_moving *= -1
                            self.enemies[index].calculate_move_col()
                self.enemies[index].set_W()

    # draw functions
    def draw_player(self, x, y):
        if self.is_legal(x, y):
            self.player.loc_w = x
            self.player.loc_h = y
        self.screen.blit(self.player.image, (self.player.loc_w, self.player.loc_h))

    def draw_enemies(self):
        for index in self.enemies:
            self.screen.blit(self.enemies[index].image, (self.enemies[index].loc_w, self.enemies[index].loc_h))

    def draw_bullets(self):
        for bullet in self.bullets:
            self.screen.blit(bullet.image, (bullet.loc_w, bullet.loc_h))

    def move_and_delete_bullets(self):
        index_to_remove = []
        for i in range(0, len(self.bullets)):
            self.bullets[i].calculate_move_row()
            if self.bullets[i].pre_loc_h < 0:
                index_to_remove.append(i)
            else:
                self.bullets[i].set_H()
        for index in index_to_remove:
            self.bullets.pop(index)

    def move_and_draw_enemies(self):
        self.move_enemies()
        self.draw_enemies()

    def bullet_hit(self):
        bullet_to_remove = []
        enemies_to_remove = []
        for i in range(0, len(self.bullets)):
            for index in self.enemies:
                if Utils.is_collision(self.bullets[i], self.enemies[index]):
                    bullet_to_remove.append(i)
                    enemies_to_remove.append(index)
        for i in bullet_to_remove:
            self.bullets.pop(i)

        for index in enemies_to_remove:
            self.enemies.pop(index)
            self.score_value += 1

    def init_enemies(self):
        # init the enemies
        for i in range(0, 4):
            self.enemies[i] = self.enemy_factory.create_enemy("enemy - regular", 120 + 150 * i, 70, i)

    def enemy_hit_the_player(self):
        for index_enemy in self.enemies:
            if Utils.is_collision(self.player, self.enemies[index_enemy]):
                return True
        return False

    def handle_keyboard_down_event(self, event):
        if event.key == self.pygame.K_LEFT:
            self.player.direction_w = -1
            self.player.direction_h = 0
            self.player.is_moving = True
        elif event.key == self.pygame.K_RIGHT:
            self.player.direction_w = 1
            self.player.direction_h = 0
            self.player.is_moving = True
        elif event.key == self.pygame.K_UP:
            self.player.direction_h = -1
            self.player.direction_w = 0
            self.player.is_moving = True
        elif event.key == self.pygame.K_DOWN:
            self.player.direction_h = 1
            self.player.direction_w = 0
            self.player.is_moving = True
        elif event.key == self.pygame.K_SPACE:
            if self.player.try_to_shot(self.bullets) is True:
                self.bullets.append(
                    self.enemy_factory.create_bullet("bullet_1", self.player.loc_w, self.player.loc_h))

    def handle_keyboard_up_event(self, event):
        if event.key == self.pygame.K_LEFT or event.key == self.pygame.K_RIGHT:
            self.player.is_moving = False
        if event.key == self.pygame.K_UP or event.key == self.pygame.K_DOWN:
            self.player.is_moving = False

    def move_player(self):
        self.player.calculate_move_row()
        self.player.calculate_move_col()

        if self.is_legal(self.player.pre_loc_w, self.player.pre_loc_h):
            self.player.set_W()
            self.player.set_H()

    def run_loop(self):
        # RGB - Red, Green, Blue
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.background_img, (0, 0))

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                return True
            if event.type == self.pygame.KEYDOWN:
                self.handle_keyboard_down_event(event)
            if event.type == self.pygame.KEYUP:
                self.handle_keyboard_up_event(event)

        if self.player.is_moving:
            self.move_player()

        self.draw_player(self.player.loc_w, self.player.loc_h)

        if self.enemy_hit_the_player():
            return True

        self.move_and_draw_enemies()
        self.move_and_delete_bullets()
        self.draw_bullets()
        self.bullet_hit()
        self.show_score(self.text_w, self.text_h)
        self.display.update()
        return False  # not quit the game
