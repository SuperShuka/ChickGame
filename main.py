import imports
import pygame
pygame.init()

W = 1000
H = 750

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

pygame.mixer.music.load('Assets/Sounds/LoopLepr.mp3')
chickleft = pygame.image.load('Assets/Images/chickleft.png')
chickright = pygame.image.load('Assets/Images/chickright.png')
chickjumpright = pygame.image.load('Assets/Images/chickjumpright.png')
chickjumpleft = pygame.image.load('Assets/Images/chickjumpleft.png')
chickrunleft1 = pygame.image.load('Assets/Images/chickrunleft1.png')
chickrunleft2 = pygame.image.load('Assets/Images/chickrunleft2.png')
chickrunright1 = pygame.image.load('Assets/Images/chickrunright1.png')
chickrunright2 = pygame.image.load('Assets/Images/chickrunright2.png')
flyleft1 = pygame.image.load('Assets/Images/chickflyleftst1.png')
flyleft2 = pygame.image.load('Assets/Images/chickflyleftst2.png')
flyleft3 = pygame.image.load('Assets/Images/chickflyleftst3.png')
flyright1 = pygame.image.load('Assets/Images/chickflyrightst1.png')
flyright2 = pygame.image.load('Assets/Images/chickflyrightst2.png')
flyright3 = pygame.image.load('Assets/Images/chickflyrightst3.png')
islepict = pygame.image.load('Assets/Images/testisland.png')
spikeimage = pygame.image.load('Assets/Images/spike.png')
dead = pygame.image.load('Assets/Images/Chickdeatheffect.png')


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (174, 174, 255)
BLACK = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

x = W//2
y = H-50
chickimage = chickright
jumpmove = 0
springmove = 0
speed = 5
gravity = 6
ground = H-50
jump_height = 200
chickturnr = 0
runanim = 1
flyanim = 1
jumpspeed = 10

tile_size = 50


hero = pygame.Surface((42, 46))
chicklegs = pygame.Surface((10, 15))
spike = pygame.Surface((52, 46))
island = pygame.Surface((185, 50))
island.blit(islepict, (0, 0))
world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class World:
    def __init__(self, data):
        self.tile_list = []

        dirt = pygame.image.load('Assets/Images/earthblock.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = col_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

    def draw(self):
        for tile in self.tile_list:
            sc.blit(tile[0], tile[1])
            pygame.draw.rect(sc, (255, 255, 255), tile[1], 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.K_ESCAPE:
            exit()

    keys = pygame.key.get_pressed()

    islerect = island.get_rect(bottomleft=(W // 2 + 300, H - 150))
    spikerect = spike.get_rect(bottomleft=(islerect.x+50, islerect.top))
    hrect = hero.get_rect(bottomleft=(x, y))
    legrect = chicklegs.get_rect(topleft=(x + 15, y))
    "Обрабатываем прыжок и полёт"
    if keys[pygame.K_SPACE] and ground == hrect.bottom:
        jumpmove = jump_height
    "Падение"
    if y < ground and jumpmove == 0 and springmove == 0:
        if keys[pygame.K_SPACE]:
            y += gravity // 3
        else:
            if ground - jump_height <= 5:
                y += gravity // 6
            elif ground - jump_height <= 10:
                y += gravity // 3
            else:
                if y + gravity > ground:
                    y = ground
                else:
                    y += gravity
    "Фиксить проваливание под землю БОЛЬШЕ НЕ НУЖНО УРАААААА!!!!!!"
    "Двигаем по Y"
    if jumpmove > 0:
        if jumpmove < 5:
            y -= jumpspeed // 10
            jumpmove -= jumpspeed // 10
        elif jumpmove < 10:
            y -= jumpspeed // 5
            jumpmove -= jumpspeed // 5
        elif jumpmove < 25:
            y -= jumpspeed // 2
            jumpmove -= jumpspeed // 2
        elif jumpmove < 35:
            y -= jumpspeed * 0.8 // 1
            jumpmove -= jumpspeed * 0.8 // 1
        else:
            y -= jumpspeed
            jumpmove -= jumpspeed

    if springmove > 0:
        jumpmove = 0

    "Движение по X"
    if keys[pygame.K_a] and keys[pygame.K_d]:
        x = x
        running = False
    elif keys[pygame.K_a]:
        if hrect.bottom == ground:
            x -= speed
        elif keys[pygame.K_SPACE]:
            x -= speed / 2
        else:
            x -= speed / 1.5
        chickturnr = False
        running = True
    elif keys[pygame.K_d]:
        if hrect.bottom == ground:
            x += speed
        elif keys[pygame.K_SPACE]:
            x += speed / 2
        else:
            x += speed / 1.5
        chickturnr = True
        running = True
    else:
        running = False

    # проваливание вправо и влево
    # if x <= 0:
    #     x = 0
    # if x >= 1000:
    #     x = 1000

    "Анимация"
    # При беге
    if hrect.bottom == ground and not keys[pygame.K_SPACE]:
        if running:
            if runanim <= 5:
                if chickturnr:
                    chickimage = chickrunright1
                else:
                    chickimage = chickrunleft1
                runanim += 1
            elif runanim <= 10:
                if chickturnr:
                    chickimage = chickrunright2
                else:
                    chickimage = chickrunleft2
                runanim += 1
            elif runanim > 10:
                runanim = 1
        else:
            if chickturnr:
                chickimage = chickright
            else:
                chickimage = chickleft
    # При полёте
    if not hrect.bottom == ground:
        if not jumpmove == 0 or not springmove == 0:
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

    if islerect.colliderect(legrect) and legrect.y <= islerect.top:
        ground = islerect.top
    else:
        ground = H - 50

    if spikerect.collidepoint(hrect.center):
        chickimage = dead
        pygame.mixer.music.play()
        for i in range(60):
            y -= 1
            hrect = hero.get_rect(bottomleft=(x, y))
            chickimage = dead
            sc.fill(LIGHT_BLUE)
            sc.blit(island, islerect)
            sc.blit(chickimage, hrect)
            sc.blit(spikeimage, spikerect)
            world = World(world_data)
            world.draw()
            pygame.display.update()
            clock.tick(120)
        chickturnr = 0
        x = W // 2
        y = H - 50
        chickimage = chickright
        jumpmove = 0
        springmove = 0
        hrect = hero.get_rect(bottomleft=(x, y))

    sc.fill(LIGHT_BLUE)
    sc.blit(island, islerect)
    sc.blit(chickimage, hrect)
    sc.blit(spikeimage, spikerect)
    world = World(world_data)
    world.draw()
    pygame.display.update()

    clock.tick(FPS)
