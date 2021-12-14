import pygame
from imports import sc

pygame.init()

tile_size = 50


class World:
    def __init__(self, data):
        self.tile_list = []

        dirt = pygame.image.load('Assets/Images/earthblock.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = col_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

    def draw(self):
        for tile in self.tile_list:
            sc.blit(tile[0], tile[1])
            pygame.draw.rect(sc, (255, 255, 255), tile[1], 2)
