import pygame
pygame.init()

W = 1000
H = 800
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

chickleft = pygame.image.load('Assets/Images/chickleft.png')
chickright = pygame.image.load('Assets/Images/chickright.png')
chickjumpright = pygame.image.load('Assets/Images/chickjumpright.png')
chickjumpleft = pygame.image.load('Assets/Images/chickjumpleft.png')
chickrunleft = pygame.image.load('Assets/Images/chickrunleft.png')
chickrunright = pygame.image.load('Assets/Images/chickrunright.png')
flyleft1 = pygame.image.load('Assets/Images/chickflyleftst1.png')
flyleft2 = pygame.image.load('Assets/Images/chickflyleftst2.png')
flyleft3 = pygame.image.load('Assets/Images/chickflyleftst3.png')
flyright1 = pygame.image.load('Assets/Images/chickflyrightst1.png')
flyright2 = pygame.image.load('Assets/Images/chickflyrightst2.png')
flyright3 = pygame.image.load('Assets/Images/chickflyrightst3.png')


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

x = W//2
y = H-50
chickimage = chickright
jumpmove = 0
springmove = 0
speed = 5
ground = H-50
jump_height = 100
chickturn = 0
runanim = 0
flyanim = 0

hero = pygame.Surface((42, 46))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.K_ESCAPE:
            exit()

    keys = pygame.key.get_pressed()
    hrect = hero.get_rect(bottomleft=(x, y))
    "Обрабатываем прыжок и полёт"
    if keys[pygame.K_SPACE] and ground == hrect.bottom:
        jumpmove = jump_height
    "Падение"
    if y < ground and jumpmove == 0 and springmove == 0:
        if keys[pygame.K_SPACE]:
            y += 2
        else:
            y += 5
    "Фиксим проваливание под землю"
    if y > ground:
        y = ground
    "Двигаем по Y"
    if jumpmove > 0:
        y -= 5
        jumpmove -= 5
    "Отладка"
    print(y, x, ground, jumpmove)

    "Движение по X"
    if keys[pygame.K_a] and keys[pygame.K_d]:
        x = x
        running = False
    elif keys[pygame.K_a]:
        x -= speed
        chickturn = False
        running = True
    elif keys[pygame.K_d]:
        x += speed
        chickturn = True
        running = True
    else:
        running = False

    "Анимация"
    if hrect.bottom == ground:
        if running:
            if chickturn:
                chickimage = chickrunright
            else:
                chickimage = chickrunleft
        else:
            if chickturn:
                chickimage = chickright
            else:
                chickimage = chickleft

    sc.fill(BLACK)
    sc.blit(chickimage, hrect)
    pygame.display.update()

    clock.tick(FPS)
