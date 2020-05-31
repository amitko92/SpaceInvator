import pygame

# initialize the pygame app.
pygame.init()

# creating the screen.
screen = pygame.display.set_mode((800,600))

# the game loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False