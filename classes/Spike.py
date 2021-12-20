import pygame
pygame.init()


class Spike:
    def __init__(self):
        self.x = 150
        self.y = 200
        self.surf = pygame.Surface((33, 33))
        self.image = pygame.image.load('Assets/Images/spike.png')
    def draw(self):
        sc.blit
