import pygame
from pygame.locals import *
from Utilities import background
import Utilities.button
from Levels.Info import draw_info
from Utilities.button import ToolbarButton

pygame.font.init()

def go(screen, level):
    back = Utilities.button.Button(screen, "Menu", "Fonts/Manolo.ttf", 30, 30, 100, 50)
    info = Utilities.button.Button(screen, "Info", "Fonts/Manolo.ttf", 30, 100, 100, 50)
    okay = Utilities.button.Button(screen, "Rozumiem", "Fonts/Manolo.ttf", 400, 550, 400, 80)

    start = Utilities.button.Button(screen, "Start", "Fonts/Manolo.ttf", 1050, 30, 120, 50)
    stop = Utilities.button.Button(screen, "Stop", "Fonts/Manolo.ttf", 1050, 100, 120, 50)
    step = Utilities.button.Button(screen, "Krok", "Fonts/Manolo.ttf", 1050, 170, 120, 50)

    toolbar_buttons = []

    toolbar_buttons.append(ToolbarButton(screen, "Textures/Lampa1.png", 6, 602, 93, 93, 0))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Źródło1.png", 6, 701, 93, 93, 1))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Przekaźnik.png", 105, 602, 93, 93, 2))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Tranzystor000.png", 105, 701, 93, 93, 3))

    toolbar_buttons.append(ToolbarButton(screen, "Textures/OR.png", 204, 602, 93, 93, 4))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Zegar1.png", 204, 701, 93, 93, 5))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/AND.png", 303, 602, 93, 93, 6))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Włącznik.png", 303, 701, 93, 93, 7))

    toolbar_buttons.append(ToolbarButton(screen, "Textures/XOR.png", 402, 602, 93, 93, 8))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Sumator.png", 402, 701, 93, 93, 9))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/NOT.png", 501, 602, 93, 93, 10))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Usuń.png", 501, 701, 93, 93, 11))

    toolbar_buttons.append(ToolbarButton(screen, "Textures/DużySumator.png", 600, 602, 194, 192, 12))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Licznik.png", 800, 602, 194, 192, 13))
    toolbar_buttons.append(ToolbarButton(screen, "Textures/Multiplekser.png", 1000, 602, 194, 192, 14))

    if level != 0:
        show_info = True
    else:
        show_info = False

    current_item = -1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        background.draw_background(screen, 40)

        pygame.draw.rect(screen, Color(0, 0, 0), pygame.Rect(0, 596, 1200, 204), 6)
        pygame.draw.line(screen, Color(0, 0, 0), (0, 697), (599, 697), 6)
        for i in range(6):
            pygame.draw.line(screen, Color(0, 0, 0), (101 + 99 * i, 596), (101 + 99 * i, 800), 6)
        pygame.draw.line(screen, Color(0, 0, 0), (796, 596), (796, 800), 6)
        pygame.draw.line(screen, Color(0, 0, 0), (996, 596), (996, 800), 6)

        for i, toolbar_button in enumerate(toolbar_buttons):
            if toolbar_button.action():
                if current_item == i:
                    current_item = -1
                else:
                    current_item = i

        if show_info:
            draw_info(screen, level)
            if okay.action():
                show_info = False

        if back.action():
            return None
        if level != 0:
            if info.action():
                show_info = True

        if start.action():
            print("start")
        if stop.action():
            print("stop")
        if step.action():
            print("krok")

        pygame.display.flip()
