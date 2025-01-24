import pygame
from pygame.locals import *
import game
import Utilities.button
from Utilities.background import draw_background

pygame.font.init()

def go(screen):
    buttons = []
    for i in range(6):
        buttons.append(Utilities.button.Button(screen, (i + 1).__str__(), "Fonts/GregorianFLF.ttf", i * 150 + 160, 150, 130, 130))

    for i in range(6):
        buttons.append(Utilities.button.Button(screen, (i + 7).__str__(), "Fonts/GregorianFLF.ttf", i * 150 + 160, 300, 130, 130))

    for i in range(6):
        buttons.append(Utilities.button.Button(screen, (i + 13).__str__(), "Fonts/GregorianFLF.ttf", i * 150 + 160, 450, 130, 130))

    back = Utilities.button.Button(screen, "Menu", "Fonts/Manolo.ttf", 350, 650, 500, 70)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        draw_background(screen, 40, 0, 0)

        for button in buttons:
            if button.action():
                level = int(button.text)
                while game.go(screen, level):
                    level += 1
                    if level == 19:
                        break

        if back.action():
            return None

        pygame.display.flip()
