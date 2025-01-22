import pygame
from pygame.locals import *
import menu

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Gra")

icon = pygame.image.load("Textures/Lampa1.png")
pygame.display.set_icon(icon)

menu.go(screen)

pygame.quit()
