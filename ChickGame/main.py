import pygame
import ctypes
from Spike import Spike
from Chick import Chick
from ButtonTypes import Button
from Cordsave import cordsave, cordload
pygame.init()

user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(W, H)

sc = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

menuChick = pygame.image.load('Assets/Images/chickright.png').convert_alpha()
menuChick = pygame.transform.scale(menuChick, (menuChick.get_width()*3, menuChick.get_height()*3))

titleFont = pygame.font.SysFont('comicsansms', 48)
nameFont = pygame.font.SysFont('comicsansms', 96)

pygame.mixer.music.load('Assets/Sounds/Grass.mp3')
pygame.mixer.music.set_volume(0.3)
skyimg = pygame.image.load('Assets/Images/sky.png').convert_alpha()
skyimg = pygame.transform.scale(skyimg, (W, H))

pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (150, 220, 255)
BLACK = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

spikeslist = pygame.sprite.Group()
mainButts = pygame.sprite.Group()
settingButts = pygame.sprite.Group()

x, y = cordload()
hero = Chick(x, y)

spikeex = Spike(23, 65, spikeslist)
spikeex = Spike(259, H-50, spikeslist)
spikeex = Spike(593, H-95, spikeslist)
spikeex = Spike(1256, H-50, spikeslist)

playbutton = Button(mainButts, 'Играть!', 1)
settingsbutton = Button(mainButts, 'Настройки', 2)
quitbutton = Button(mainButts, 'Выйти', 3)

volumesetts = Button(settingButts, 'Настройка звука', 1)

level = pygame.Surface((W, H))
level.blit(skyimg, (0, 0))
spikeslist.draw(level)

mode = 'Main Menu'
curbutt = 1
title = titleFont.render('Главное меню', 1, BLACK)
GameName = nameFont.render('Chick Game', 1, GREEN)

while True:
    while mode == 'Game':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cordsave(hero.x, hero.y)
                    curbutt = 1
                    title = titleFont.render('Главное меню', 1, BLACK)
                    mode = 'Main Menu'
        hero.update()
        sc.blit(level, (0, 0))
        sc.blit(hero.chickimage, hero.rect)
        pygame.display.update()
        clock.tick(FPS)
    while mode == 'Main Menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if curbutt == len(mainButts):
                        curbutt = 1
                    else:
                        curbutt += 1
                if event.key == pygame.K_w:
                    if curbutt == 1:
                        curbutt = len(mainButts)
                    else:
                        curbutt -= 1
                if event.key == pygame.K_SPACE:
                    if playbutton.num == curbutt:
                        mode = 'Game'
                    if settingsbutton.num == curbutt:
                        curbutt = 1
                        title = titleFont.render('Настройки', 1, BLACK)
                        mode = 'Settings'
                    if quitbutton.num == curbutt:
                        exit()

        mainButts.update(curbutt)
        sc.blit(skyimg, (0, 0))
        sc.blit(title, (W-510, H//4-105))
        pygame.draw.line(sc, BLACK, (W-510, H//4-25), (W-175, H//4-25), 5)
        sc.blit(GameName, (50, 20))
        sc.blit(menuChick, (150, H-250))
        mainButts.draw(sc)
        pygame.display.update()
        clock.tick(FPS)

    while mode == 'Settings':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if curbutt == len(mainButts):
                        curbutt = 1
                    else:
                        curbutt += 1
                if event.key == pygame.K_w:
                    if curbutt == 1:
                        curbutt = len(mainButts)
                    else:
                        curbutt -= 1
                if event.key == pygame.K_SPACE:
                    if volumesetts.num == curbutt:
                        mode = 'game'
                    if settingsbutton.num == curbutt:
                        curbutt = 0
                        mode = 'settings'
                    if quitbutton.num == curbutt:
                        exit()

        settingButts.update(curbutt)
        sc.blit(skyimg, (0, 0))
        sc.blit(title, (W-510, H//4-105))
        pygame.draw.line(sc, BLACK, (W-510, H//4-25), (W-175, H//4-25), 5)
        sc.blit(GameName, (50, 20))
        sc.blit(menuChick, (150, H-250))
        settingButts.draw(sc)
        pygame.display.update()
        clock.tick(FPS)
