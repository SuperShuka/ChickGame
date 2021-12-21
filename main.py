import pygame
import ctypes
from Wait import wait
pygame.init()

user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(W, H)

sc = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

chicksound = pygame.mixer.Sound('Assets/Sounds/Papapapapapa.mp3')
pygame.mixer.music.load('Assets/Sounds/Grass.mp3')
skyimg = pygame.image.load('Assets/Images/sky.png')
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

pygame.mixer.music.play(-1)


def stop():
    savecords = open("Assets/Saves.txt", "w")
    savecords.write(str(int(x // 1)))
    savecords.write(', ')
    savecords.write(str(int(y // 1)))
    savecords.close()
    exit()


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (150, 220, 255)
BLACK = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

loadcords = open("Assets/Saves.txt", "r")
prevcords = loadcords.readline()
x, y = prevcords.split(',')
x, y = int(x), int(y)
loadcords.close()

chickimage = chickright
xspeed = 0
runspeed = 5
yspeed = 0
gravity = 0.7
jumpspeed = 15
acceleration = 0.5
ground = H-50
chickturnr = 0
runanim = 1
flyanim = 1
tile_size = 50
on_ice = 0

hero = pygame.Surface((42, 46))
chicklegs = pygame.Surface((10, 15))
spike = pygame.Surface((33, 33))
island = pygame.Surface((250, 30))
island.fill(GREEN)
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


class Spike:
    def __init__(self):
        self.x = 150
        self.y = 200
        self.surf = pygame.Surface((33, 33))
        self.image = pygame.image.load('Assets/Images/spike.png')

    def usespike(self):
        self.x = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stop()

    keys = pygame.key.get_pressed()

    islerect = island.get_rect(bottomleft=(W // 2 + 200, H - 100))
    spikerect = spike.get_rect(bottomleft=(islerect.x+100, islerect.top))
    hrect = hero.get_rect(bottomleft=(x, y))
    legrect = chicklegs.get_rect(topleft=(x + 15, y))

    "Обрабатываем прыжок"
    if keys[pygame.K_SPACE] and ground == hrect.bottom:
        yspeed = jumpspeed

    "Поднимаем по Y"
    if yspeed > 0:
        y -= yspeed
        yspeed -= gravity

    "Падение и полёт"
    if y < ground and yspeed <= 0:
        if keys[pygame.K_SPACE]:
            if yspeed > -2:
                yspeed -= gravity/2
            else:
                yspeed = -2
        else:
            if yspeed > -6:
                yspeed -= gravity
            else:
                yspeed = -6
        if y-yspeed >= ground:
            y = ground
            yspeed = 0
        y -= yspeed

        "Движение по X "
# ОБЕ НАЖАТЫ (Остановка)
    if keys[pygame.K_a] and keys[pygame.K_d]:
        if xspeed > 0:
            if xspeed - acceleration <= 0:
                xspeed = 0
            else:
                if hrect.bottom == ground:
                    if on_ice:
                        xspeed -= acceleration / 3
                    else:
                        xspeed -= acceleration
                elif keys[pygame.K_SPACE]:
                    xspeed -= acceleration / 1.5
                else:
                    xspeed -= acceleration / 1.25
        else:
            if xspeed + acceleration >= 0:
                xspeed = 0
            else:
                if hrect.bottom == ground:
                    if on_ice:
                        xspeed += acceleration / 3
                    else:
                        xspeed += acceleration
                elif keys[pygame.K_SPACE]:
                    xspeed += acceleration / 3
                else:
                    xspeed += acceleration / 2
# НАЛЕВО
    elif keys[pygame.K_a] and xspeed <= 0:
        if hrect.bottom == ground:
            if on_ice:
                if xspeed > -runspeed * 1.5:
                    xspeed -= acceleration / 3
            else:
                if xspeed > -runspeed:
                    xspeed -= acceleration
        elif keys[pygame.K_SPACE]:
            if xspeed > -runspeed / 2:
                xspeed -= acceleration / 3
        else:
            if xspeed > -runspeed / 1.5:
                xspeed -= acceleration / 2
        chickturnr = False
# НАПРАВО
    elif keys[pygame.K_d] and xspeed >= 0:
        if hrect.bottom == ground:
            if on_ice:
                if xspeed < runspeed * 1.5:
                    xspeed += acceleration / 3
            else:
                if xspeed < runspeed:
                    xspeed += acceleration
        elif keys[pygame.K_SPACE]:
            if xspeed < runspeed / 2:
                xspeed += acceleration / 3
        else:
            if xspeed < runspeed / 1.5:
                xspeed += acceleration / 2
        chickturnr = True
        # НЕ НАЖАТЫ (Остановка)
    else:
        if xspeed > 0:
            if xspeed - acceleration <= 0:
                xspeed = 0
            else:
                if hrect.bottom == ground:
                    if on_ice:
                        xspeed -= acceleration / 3
                    else:
                        xspeed -= acceleration
                elif keys[pygame.K_SPACE]:
                    xspeed -= acceleration / 3
                else:
                    xspeed -= acceleration / 2
        else:
            if xspeed + acceleration >= 0:
                xspeed = 0
            else:
                if hrect.bottom == ground:
                    if on_ice:
                        xspeed += acceleration / 3
                    else:
                        xspeed += acceleration
                elif keys[pygame.K_SPACE]:
                    xspeed += acceleration / 3
                else:
                    xspeed += acceleration / 2
    x += xspeed

    # проваливание вправо и влево
    # if x <= 0:
    #     x = 0
    # if x >= 1000:
    #     x = 1000

    "Анимация"
    # При беге
    if hrect.bottom == ground and not keys[pygame.K_SPACE]:
        if xspeed:
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
        if yspeed >= 0:
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
        on_ice = 1
    else:
        on_ice = 0
        ground = H - 50

    if hrect.colliderect(spikerect):
        chickimage = dead
        pygame.mixer.music.pause()
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
        exit()

    sc.fill(LIGHT_BLUE)
    sc.blit(island, islerect)
    sc.blit(chickimage, hrect)
    sc.blit(spikeimage, spikerect)
    world = World(world_data)
    world.draw()
    pygame.display.update()

    clock.tick(FPS)
