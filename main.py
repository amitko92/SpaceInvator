import pygame

from Enemy import Enemy
from Game import Game
from Hero import Player

player = Player(pygame, r'..\images\hero.png', 370, 480, 37, 2, 0, 0)
enemies = []
locations = []

for i in range(0, 4):
    enemies.append(Enemy(pygame, r'..\images\space_enemy.png', 120 + 150 * i, 70, 37, 0.5, i))
    locations.append((120 + 150 * i, 70, i))
    #  print("loc: " + str(120 + 150*i) + "index " + str(i))

game = Game(pygame, "Space Invader", r'..\images\background_1.jpg', 800, 600, r'..\images\icon.png', player, enemies,
            locations)

# initialize the pygame app.
pygame.init()

# the game loop.
running = True
while running:
    running = not (game.run_loop())
