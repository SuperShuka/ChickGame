import pygame
import ctypes
pygame.init()

user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sc = pygame.display.set_mode((W, H), pygame.FULLSCREEN)


class Chick(pygame.sprite.Sprite):

    def __init__(self, x, y):
        chickleft = pygame.image.load('Assets/Images/chickleft.png').convert_alpha()
        chickright = pygame.image.load('Assets/Images/chickright.png').convert_alpha()
        chickjumpright = pygame.image.load('Assets/Images/chickjumpright.png').convert_alpha()
        chickjumpleft = pygame.image.load('Assets/Images/chickjumpleft.png').convert_alpha()
        chickrunleft1 = pygame.image.load('Assets/Images/chickrunleft1.png').convert_alpha()
        chickrunleft2 = pygame.image.load('Assets/Images/chickrunleft2.png').convert_alpha()
        chickrunright1 = pygame.image.load('Assets/Images/chickrunright1.png').convert_alpha()
        chickrunright2 = pygame.image.load('Assets/Images/chickrunright2.png').convert_alpha()
        flyleft1 = pygame.image.load('Assets/Images/chickflyleftst1.png').convert_alpha()
        flyleft2 = pygame.image.load('Assets/Images/chickflyleftst2.png').convert_alpha()
        flyleft3 = pygame.image.load('Assets/Images/chickflyleftst3.png').convert_alpha()
        flyright1 = pygame.image.load('Assets/Images/chickflyrightst1.png').convert_alpha()
        flyright2 = pygame.image.load('Assets/Images/chickflyrightst2.png').convert_alpha()
        flyright3 = pygame.image.load('Assets/Images/chickflyrightst3.png').convert_alpha()
        dead = pygame.image.load('Assets/Images/Chickdeatheffect.png').convert_alpha()
        chicksound = pygame.mixer.Sound('Assets/Sounds/Papapapapapa.mp3')

        chickimage = chickright
        xspeed = 0
        runspeed = 5
        yspeed = 0
        gravity = 0.7
        jumpspeed = 15
        acceleration = 0.5
        ground = H - 50
        chickturnr = 0
        runanim = 1
        flyanim = 1

    def update(self):

