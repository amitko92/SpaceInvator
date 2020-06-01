import pygame

pygame.display.set_caption("Space Invader")
width = 800
Height = 600
window_size = (width, Height)
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
olive_color = (128, 128, 0)
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
movementRate = 0.3
playerX_change = 0
playerY_change = 0


def check_if_in_border(x, y):
    return 0 < y < Height and 0 < x < width


def player(x, y):
    if check_if_in_border(x, y):
        screen.blit(playerImg, (x, y))


# initialize the pygame app.
pygame.init()

# creating the screen.
screen = pygame.display.set_mode(window_size)

# the game loop.
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - movementRate
            elif event.key == pygame.K_RIGHT:
                playerX_change = movementRate
            elif event.key == pygame.K_UP:
                playerY_change = - movementRate
            elif event.key == pygame.K_DOWN:
                playerY_change = movementRate

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    if check_if_in_border(playerX + playerX_change, playerY + playerY_change):
        playerX += playerX_change
        playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
