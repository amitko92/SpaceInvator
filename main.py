import pygame
from Hero import Player
from Game import Game

# spaceship_url = r'C:\Users\amitk\Documents\github repository\SpaceInvader\spaceship.png'
# icon_url = r'C:\Users\amitk\Documents\github repository\SpaceInvader\ufo.png'

player = Player(pygame, r'..\spaceship.png', 370, 480, 0.3, 0, 0)
game = Game(pygame, "Space Invader", 800, 600, r'..\ufo.png', player)

# initialize the pygame app.
pygame.init()

# the game loop.
running = True
while running:
    running = not(game.run_loop())
