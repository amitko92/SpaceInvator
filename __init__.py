import pygame

# initialize the pygame app.
from Enemy_factory import Factory
from Hero import Player

# init the pygame
pygame.init()

player = Player(370, 480, 37, 2, pygame.image.load('hero.png'), 0, 0)

images = {"enemy - regular": pygame.image.load('space_enemy.png'),
          "bullet_1": pygame.image.load('bullet_2.png')}

movement_rate = {"enemy - regular": 0.7,
                 'bullet_1': 1.2}

rs = {"enemy - regular": 56,
      'bullet_1': 20}

factory = Factory(images, movement_rate, rs)


