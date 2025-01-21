import pygame
from pygame.locals import *

from Utilities import background
import Utilities.button

pygame.font.init()

def go(screen, level):
    back = Utilities.button.Button(screen, "Menu", "Fonts/Manolo.ttf", 30, 30, 100, 50)
    info = Utilities.button.Button(screen, "Info", "Fonts/Manolo.ttf", 30, 100, 100, 50)

    start = Utilities.button.Button(screen, "Start", "Fonts/Manolo.ttf", 1050, 30, 120, 50)
    stop = Utilities.button.Button(screen, "Stop", "Fonts/Manolo.ttf", 1050, 100, 120, 50)
    step = Utilities.button.Button(screen, "Krok", "Fonts/Manolo.ttf", 1050, 170, 120, 50)

    show_info = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        background.draw_background(screen, 40)

        if back.action():
            return None
        if info.action():
            show_info = True

        if start.action():
            print("start")
        if stop.action():
            print("stop")
        if step.action():
            print("krok")

        pygame.display.flip()
