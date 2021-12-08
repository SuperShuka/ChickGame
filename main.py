import pygame
pygame.init()

W = 1500
H = 1000
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

chickleft = pygame.image.load('Assets/Images/chickleft.png')
chickright = pygame.image.load('Assets/Images/chickright.png')
chickleft = pygame.image.load('Assets/Images/chickjumpleft.png')
chickright = pygame.image.load('Assets/Images/chickright.png')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

ground = 50
yspeed = 0
xspeed = 0
jump_height = 50

you =


def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and ground==:



FPS = 90
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.K_ESCAPE:
            exit()

    clock.tick(FPS)
