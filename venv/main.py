import pygame

# initialize the pygame app.
pygame.init()

# creating the screen.
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
olive_color = (128, 128, 0)

# the game loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # RGB - Red, Green, Blue
        screen.fill(olive_color)
        pygame.display.update()