import pygame
clock = pygame.time.Clock()


def wait(time):
    i = 0
    while i <= time:
        i += 1
        clock.tick(1)
