import pygame
import ctypes
from Spike import Spike
from Chick import Chick
from Wait import wait
from ButtonTypes import Button
import Saving
pygame.init()

user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

sc = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

menuChick = pygame.image.load('Assets/Images/chickright.png').convert_alpha()
menuChick = pygame.transform.scale(menuChick, (menuChick.get_width()*3, menuChick.get_height()*3))

titleFont = pygame.font.SysFont('comicsansms', 48)
nameFont = pygame.font.SysFont('comicsansms', 96)

effectsvolume, musicvolume = Saving.volumesettings_load()
pygame.mixer.music.load('Assets/Sounds/Grass.mp3')
pygame.mixer.music.set_volume(musicvolume)

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

spikes_Group = pygame.sprite.Group()
mainButts_Group = pygame.sprite.Group()
settingButts_Group = pygame.sprite.Group()
settings_sliders_Group = pygame.sprite.Group()

x, y = W//2,  H-50
hero = Chick(x, y)

makeSpike = Spike(23, 65, spikes_Group)
makeSpike = Spike(259, H - 50, spikes_Group)
makeSpike = Spike(593, H - 95, spikes_Group)
makeSpike = Spike(1256, H - 50, spikes_Group)
spikes_rect_list = []

play_button = Button(mainButts_Group, 'Играть!', 1)
settings_button = Button(mainButts_Group, 'Настройки', 2)
quit_button = Button(mainButts_Group, 'Выйти', 3)

settings_Back_button = Button(settingButts_Group, 'Назад', 1)
musicvolume_setts_button = Button(settingButts_Group, 'Громкость музыки', 2)
soundeffect_volume_setts_button = Button(settingButts_Group, 'Громкость эффектов', 3)
secret_button = Button(settingButts_Group, 'Секретная настройка', 4)

music_volume_slider_exist = soundeffect_volume_slider_exist = False
level = pygame.Surface((W, H))
level.blit(skyimg, (0, 0))
spikes_Group.draw(level)

for spike in spikes_Group:
    spikes_rect_list.append(spike.rect)


def game_draw():
    hero.update()
    sc.blit(level, (0, 0))
    sc.blit(hero.chickimage, hero.rect)
    pygame.display.update()


def mainmenu_draw():
    mainButts_Group.update(curbutt_num)
    sc.blit(skyimg, (0, 0))
    sc.blit(title, (W - 510, H // 4 - 105))
    pygame.draw.line(sc, BLACK, (W - 510, H // 4 - 25), (W - 175, H // 4 - 25), 5)
    sc.blit(GameName, (50, 20))
    sc.blit(menuChick, (150, H - 250))
    mainButts_Group.draw(sc)
    pygame.display.update()


def settings_draw():
    settingButts_Group.update(curbutt_num)
    sc.blit(skyimg, (0, 0))
    sc.blit(title, (W - 510, H // 4 - 105))
    pygame.draw.line(sc, BLACK, (W - 510, H // 4 - 25), (W - 175, H // 4 - 25), 5)
    sc.blit(GameName, (50, 20))
    sc.blit(menuChick, (150, H - 250))
    settingButts_Group.draw(sc)
    settings_sliders_Group.draw(sc)
    pygame.display.update()


mode = 'Main Menu'
curbutt_num = 1
title = titleFont.render('Главное меню', True, BLACK)
GameName = nameFont.render('Chick Game', True, GREEN)

while True:
    """Игра"""
    while mode == 'Game':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    curbutt_num = 1
                    title = titleFont.render('Главное меню', True, BLACK)
                    mode = 'Main Menu'
                    break
        for spike in spikes_Group:
            if hero.rect.colliderect(spike.rect):
                curbutt_num = 1
                title = titleFont.render('Главное меню', True, BLACK)
                mode = 'Main Menu'
                hero.x, hero.y = W // 2, H - 50
                print('die')
                break
        game_draw()
        clock.tick(FPS)
    """Главное меню"""
    while mode == 'Main Menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if curbutt_num == len(mainButts_Group):
                        curbutt_num = 1
                    else:
                        curbutt_num += 1
                if event.key == pygame.K_w:
                    if curbutt_num == 1:
                        curbutt_num = len(mainButts_Group)
                    else:
                        curbutt_num -= 1
                if event.key == pygame.K_SPACE:
                    if play_button.num == curbutt_num:
                        mode = 'Game'
                        wait(1)
                        break
                    if settings_button.num == curbutt_num:
                        curbutt_num = 1
                        title = titleFont.render('Настройки', True, BLACK)
                        mode = 'Settings'
                        break
                    if quit_button.num == curbutt_num:
                        exit()
        mainmenu_draw()
        clock.tick(FPS)
    """Настройки"""
    while mode == 'Settings':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if curbutt_num == len(settingButts_Group):
                        curbutt_num = 1
                    else:
                        curbutt_num += 1
                if event.key == pygame.K_w:
                    if curbutt_num == 1:
                        curbutt_num = len(settingButts_Group)
                    else:
                        curbutt_num -= 1
                if event.key == pygame.K_SPACE:
                    if settings_Back_button.num == curbutt_num:
                        curbutt_num = 2
                        title = titleFont.render('Главное меню', True, BLACK)
                        mode = 'Main Menu'
                        break
                    if musicvolume_setts_button.num == curbutt_num:
                        music_volume_slider_exist = True
                    if soundeffect_volume_setts_button.num == curbutt_num:
                        soundeffect_volume_slider_exist = True
        if music_volume_slider_exist:
            wait(1)
            musicvolume_setts_button.kill()
            while music_volume_slider_exist:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            musicvolume_setts_button.add(settingButts_Group)
                            music_volume_slider_exist = False
                settings_draw()
        if soundeffect_volume_slider_exist:
            wait(1)
            soundeffect_volume_setts_button.kill()
            while soundeffect_volume_slider_exist:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            soundeffect_volume_setts_button.add(settingButts_Group)
                            soundeffect_volume_slider_exist = False
                settings_draw()
        settings_draw()
        clock.tick(FPS)
