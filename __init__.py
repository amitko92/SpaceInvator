import pygame

# initialize the pygame app.
from Enemy_factory import Factory
from Hero import Player

# init the pygame
pygame.init()

player = Player(width=370, height=480, r=37, movement_rate_w=2, movement_rate_h=2, player_img=pygame.image.load('hero.png'))

images = {"enemy - regular": pygame.image.load('space_enemy.png'),
          "bullet_1": pygame.image.load('bullet_2.png')}

movement_rate_w = {"enemy - regular": 0.7,
                   'bullet_1': -1.2}

movement_rate_h = {"enemy - regular": 70,
                   'bullet_1': -1.2}

rs = {"enemy - regular": 56,
      'bullet_1': 20}

factory = Factory(images, movement_rate_w, movement_rate_h, rs)
