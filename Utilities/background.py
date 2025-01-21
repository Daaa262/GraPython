import pygame
from pygame import Color

def draw_background(screen, dot_space):
    screen.fill(Color(200, 200, 200))
    for x in range(screen.get_size()[0] // dot_space + 1):
        for y in range(screen.get_size()[1] // dot_space + 1):
            pygame.draw.circle(screen, Color(100, 100, 100), (x * dot_space + dot_space // 2, y * dot_space + dot_space // 2), 1)