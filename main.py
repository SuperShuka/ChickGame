import pygame
import ctypes
from Spike import Spike
from Spike import spikeslist
from Chick import Chick
from Wait import wait
pygame.init()

user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(W, H)

sc = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
pygame.display.set_caption('Chick Game')
pygame.display.set_icon(pygame.image.load('Assets/Images/chickright.png'))

pygame.mixer.music.load('Assets/Sounds/Grass.mp3')
pygame.mixer.music.set_volume(0.3)
skyimg = pygame.image.load('Assets/Images/sky.png').convert_alpha()
islepict = pygame.image.load('Assets/Images/testisland.png').convert_alpha()

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

hero = Chick(x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stop()

    hero.update()

    sc.fill(LIGHT_BLUE)
    sc.blit(hero.image, hero.rect)
    pygame.display.update()

    clock.tick(FPS)
