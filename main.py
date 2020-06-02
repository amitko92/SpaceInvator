import pygame
from Hero import Player
from Game import Game
from Enemy import Enemy

# spaceship_url = r'C:\Users\amitk\Documents\github repository\SpaceInvader\spaceship.png'
# icon_url = r'C:\Users\amitk\Documents\github repository\SpaceInvader\icon.png'
player = Player(pygame, r'..\images\hero.png', 370, 480, 0.3, 0, 0)
enemies = []
locations = []
for i in range(0, 4):
    enemies.append(Enemy(pygame, r'..\images\space_enemy.png', 120 + 150*i, 70, 0.1, i))
    locations.append((120 + 150*i, 70, i))
    #  print("loc: " + str(120 + 150*i) + "index " + str(i))

game = Game(pygame, "Space Invader", 800, 600, r'..\images\icon.png', player, enemies, locations)

# initialize the pygame app.
pygame.init()

# the game loop.
running = True
while running:
    running = not (game.run_loop())
