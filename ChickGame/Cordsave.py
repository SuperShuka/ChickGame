import pygame
pygame.init()


def cordload():
    loadcords = open("Assets/Saves.txt", "r")
    prevcords = loadcords.readline()
    x, y = prevcords.split(',')
    x, y = int(x), int(y)
    loadcords.close()
    return x, y


def cordsave(x, y):
    savecords = open("Assets/Saves.txt", "w")
    savecords.write(str(int(x // 1)))
    savecords.write(', ')
    savecords.write(str(int(y // 1)))
    savecords.close()
