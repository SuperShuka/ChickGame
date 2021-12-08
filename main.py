import pygame
pygame.init()

W = 1500
H = 1000
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

jump_height = 50

FPS = 90
clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.K_ESCAPE:
            exit()

    sc.fill(BLACK)
    pygame.display.update()

    clock.tick(FPS)
