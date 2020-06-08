import pygame
from Game import Game
from Hero import Player
from Enemy_factory import Factory
import __init__

game = Game(pygame, "Space Invader", 'background_1.jpg', 800, 600, 'icon.png', __init__.player, __init__.factory)

# the game loop.
running = True
while running:

    running = not (game.run_loop())
