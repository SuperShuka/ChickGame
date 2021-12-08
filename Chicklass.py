import pygame
W = 1500
H = 1000
sc = pygame.display.set_mode((W, H))


class Chick:
    """Персонаж"""
    def __init__(self):
        self.photo = pygame.image.load('Assets/Images/Chick.png')
        self.surf = pygame.Surface((60, 80))
        self.rect = self.surf.get_rect(center=(W//2, H-80))
        sc.blit(self.photo, self.rect.bottom)

    def move(self):
