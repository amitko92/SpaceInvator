import pygame

# initialize the pygame app.
from Enemy_factory import Factory
from Hero import Player

# init the pygame
pygame.init()


player = Player(370, 480, 4, 4, pygame.image.load('hero.png'), 32, 32)

images = {"enemy - regular": pygame.image.load('space_enemy.png'),
          "bullet_1": pygame.image.load('bullet_2.png')}

movement_rate_w = {"enemy - regular": 1.4,
                   'bullet_1': -2}

movement_rate_h = {"enemy - regular": 70,
                   'bullet_1': -2}

size_w = {"enemy - regular": 32,
                   'bullet_1': 32}

size_h = {"enemy - regular": 32,
                   'bullet_1': 32}

factory = Factory(images, movement_rate_w, movement_rate_h, size_w, size_h)
