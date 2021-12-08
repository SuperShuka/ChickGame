import pygame
pygame.init()

W = 1500
H = 1000
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

chickleft = pygame.image.load('Assets/Images/chickleft.png')
chickright = pygame.image.load('Assets/Images/chickright.png')
chickjumpright = pygame.image.load('Assets/Images/chickjumpleft.png')
chickjumpleft = pygame.image.load('Assets/Images/chickjumpright.png')
chickrunleft = pygame.image.load('Assets/Images/chickrunleft.png')
chickrunright = pygame.image.load('Assets/Images/chickrunright.png')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

ground = 50
jump_height = 50
chickturn = 0

hero = pygame.Surface((42, 46))


def move(x, y, xspeed, yspeed, chickimage):
    keys = pygame.key.get_pressed()
    hrect = hero.get_rect(bottom=(x, y))
    if keys[pygame.K_SPACE] and ground == hrect.bottom:
        yspeed = jump_height
    if yspeed > 0:
        if chickturn == 1:
            chickimage = chickjumpright
        else:
            chickimage = chickjumpleft
        y += 1
        yspeed -= 1
    if y > ground:
        if chickturn == 1:
            chickimage = chickjumpright
        else:
            chickimage = chickjumpleft



FPS = 90
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.K_ESCAPE:
            exit()

    clock.tick(FPS)
