import pygame
from moviepy.editor import *
import ctypes
user32 = ctypes.windll.user32
W, H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.init()

secret_clip = VideoFileClip("Assets\\Images\\secret.mp4", target_resolution=(H, W))
