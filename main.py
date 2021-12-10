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
jump_height = 200
chickturnr = 0
runanim = 1
flyanim = 1

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
        if jumpmove < 5:
            y -= 1
            jumpmove -= 1
        elif jumpmove < 10:
            y -= 2
            jumpmove -= 2
        elif jumpmove < 25:
            y -= 5
            jumpmove -= 5
        elif jumpmove < 35:
            y -= 8
            jumpmove -= 8
        else:
            y -= 10
            jumpmove -= 10

    if springmove > 0:
        jumpmove = 0

    "Движение по X"
    if keys[pygame.K_a] and keys[pygame.K_d]:
        x = x
        running = False
    elif keys[pygame.K_a]:
        x -= speed
        chickturnr = False
        running = True
    elif keys[pygame.K_d]:
        x += speed
        chickturnr = True
        running = True
    else:
        running = False

    "Анимация"
    # При беге
    if hrect.bottom == ground:
        if running:
            if chickturnr:
                chickimage = chickrunright
            else:
                chickimage = chickrunleft
        else:
            if chickturnr:
                chickimage = chickright
            else:
                chickimage = chickleft
    # При полёте
    if not hrect.bottom == ground:
        if not jumpmove == 0 and not springmove == 0:
            if chickturnr:
                chickimage = chickjumpright
            else:
                chickimage = chickjumpleft
        elif keys[pygame.K_SPACE]:
            if chickturnr:
                if flyanim <= 10:
                    chickimage = flyright1
                    flyanim += 1
                elif 10 < flyanim <= 20:
                    chickimage = flyright2
                    flyanim += 1
                elif 20 < flyanim <= 30:
                    chickimage = flyright3
                    flyanim += 1
                elif 30 < flyanim < 35:
                    chickimage = flyright2
                    flyanim += 1
                elif flyanim == 35:
                    flyanim = 1
            else:
                if flyanim <= 10:
                    chickimage = flyleft1
                    flyanim += 1
                elif 10 < flyanim <= 20:
                    chickimage = flyleft2
                    flyanim += 1
                elif 20 < flyanim <= 30:
                    chickimage = flyleft3
                    flyanim += 1
                elif 30 < flyanim < 35:
                    chickimage = flyleft2
                    flyanim += 1
                elif flyanim == 35:
                    flyanim = 1
        else:
            if chickturnr:
                chickimage = chickjumpright
            else:
                chickimage = chickjumpleft

    sc.fill(BLACK)
    sc.blit(chickimage, hrect)
    pygame.display.update()

    clock.tick(FPS)
