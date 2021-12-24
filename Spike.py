import pygame
pygame.init()

spikeslist = pygame.sprite.Group()


class Spike(pygame.sprite.Sprite):
    def __init__(self, sx, sy):
        self.x = sx
        self.y = sy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/Images/spike.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        self.add(spikeslist)
