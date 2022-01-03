import pygame
import ctypes
user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Button(pygame.sprite.Sprite):
    def __init__(self, group, text, num):
        self.text = text
        self.num = num
        self.x = W-500
        self.y = H//4 + 86*(self.num-1)
        self.font = pygame.font.SysFont('comicsansms', 36)
        pygame.sprite.Sprite.__init__(self)
        self.image = self.font.render(self.text, True, BLACK)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.add(group)

    def update(self, curnum):
        if curnum == self.num:
            self.image = self.font.render(self.text, True, WHITE, BLACK)
        else:
            self.image = self.font.render(self.text, True, BLACK)


class Slider(pygame.sprite.Sprite):
    def __init__(self, num, value):
        self.font = pygame.font.SysFont('comicsansms', 36)
        self.num = num
        self.value = value
        self.x = W - 500
        self.y = H // 4 + 86 * (self.num - 1)
        self.surf = pygame.Surface((350, 36))
        pygame.sprite.Sprite.__init__(self)
        self.image = self.surf
        self.rect = self.surf.get_rect(topleft=(self.x, self.y))

    def update(self, value):
        None


