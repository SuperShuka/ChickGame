import pygame
from main import sc

pygame.init()

# враг
"""class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_right = []
        self.image_left = []
        for i in range(1, 5):
            img_right = pygame.image.load(f'Assets/Images/slimeenemyright{i}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_right_rect = img_right.get_rect()
            img_left = pygame.image.load(f'Assets/Images/slimeenemyleft{i}.png')
            img_left_rect = img_left.get_rect()
            self.image_right.append(img_right_rect)
            self.image_left.append(img_left_rect)
        self.image = self.image_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.jumped = False

    def draw(self, x, y):
        x = """