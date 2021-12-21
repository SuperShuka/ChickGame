import pygame
pygame.init()


class Spike:
    def __init__(self, sx, sy):
        self.x = sx
        self.y = sy
        self.surf = pygame.Surface((33, 33))
        self.image = pygame.image.load('Assets/Images/spike.png')

    def usespike(self):
        self.sx
