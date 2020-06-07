import pygame
from Game import Game
from Hero import Player
from Enemy_factory import Factory

# initialize the pygame app.
pygame.init()

player = Player(370, 480, 37, 2, pygame.image.load('hero.png'), 0, 0)

images = {"enemy - regular": pygame.image.load('space_enemy.png'),
          "bullet_1": pygame.image.load('bullet_2.png')}

movement_rate = {"enemy - regular": 0.7,
                 'bullet_1': 1.2}

rs = {"enemy - regular": 31,
      'bullet_1': 20}

factory = Factory(images, movement_rate, rs)

game = Game(pygame, "Space Invader", 'background_1.jpg', 800, 600, 'icon.png', player, factory)

# the game loop.
running = True
while running:
    running = not (game.run_loop())
