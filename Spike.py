import pygame
pygame.init()


class Spike(pygame.sprite.Sprite):
    def __init__(self, sx, sy):

        self.image = pygame.image.load('Assets/Images/spike.png')

    def usespike(self):
        self.rect =
