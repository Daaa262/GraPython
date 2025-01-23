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

    if level == 0 or level >= 4:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Usuń.png", 501, 701, 93, 93, 0))
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Lampa1.png", 6, 602, 93, 93, 1))
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Źródło1.png", 6, 701, 93, 93, 2))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 501, 701, 93, 93, 0))
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 6, 602, 93, 93, 1))
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 6, 701, 93, 93, 2))

    if level == 0 or level >= 5:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Przekaźnik.png", 105, 602, 93, 93, 3))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 105, 602, 93, 93, 3))

    if level == 0 or level >= 6:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Tranzystor000.png", 105, 701, 93, 93, 4))
        toolbar_buttons.append(ToolbarButton(screen, "Textures/OR.png", 204, 602, 93, 93, 5))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 105, 701, 93, 93, 4))
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 204, 602, 93, 93, 5))

    if level == 0 or level >= 7:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/NOT.png", 501, 602, 93, 93, 6))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 501, 602, 93, 93, 6))

    if level == 0 or level >= 8:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Zegar1.png", 204, 701, 93, 93, 7))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 204, 701, 93, 93, 7))

    if level == 0 or level >= 9:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/AND.png", 303, 602, 93, 93, 8))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 303, 602, 93, 93, 8))

    if level == 0 or level >= 11:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Włącznik.png", 303, 701, 93, 93, 9))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 303, 701, 93, 93, 9))

    if level == 0 or level >= 12:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/XOR.png", 402, 602, 93, 93, 10))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 402, 602, 93, 93, 10))

    if level == 0 or level >= 13:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Sumator.png", 402, 701, 93, 93, 11))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 402, 701, 93, 93, 11))

    if level == 0 or level >= 15:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/DużySumator.png", 600, 602, 194, 192, 12))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 600, 602, 194, 192, 12))

    if level == 0 or level >= 16:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Licznik.png", 800, 602, 194, 192, 13))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 800, 602, 194, 192, 13))

    if level == 0 or level >= 17:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Multiplekser.png", 1000, 602, 194, 192, 14))
    else:
        toolbar_buttons.append(ToolbarButton(screen, "Textures/Locked.png", 1000, 602, 194, 192, 14))

    if level != 0:
        show_info = True
        drag_ready = False
    else:
        show_info = False
        drag_ready = True

    position_x, position_y = 0, 0
    current_item = None

    left_mouse_pressed = False
    pressed_x, pressed_y = 0, 0
    offset_x, offset_y = 0, 0

    image = None

    elements = []
    element_placed = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_TAB and left_mouse_pressed is False:
                    position_x = 0
                    position_y = 0
            if drag_ready is True and pygame.mouse.get_pressed(3)[0] and pygame.mouse.get_pos()[1] < 600:
                if not left_mouse_pressed:
                    left_mouse_pressed = True
                    pressed_x, pressed_y = pygame.mouse.get_pos()
                else:
                    offset_x, offset_y = pressed_x - pygame.mouse.get_pos()[0], pressed_y - pygame.mouse.get_pos()[1]
            if current_item is not None and pygame.mouse.get_pressed(3)[0] and pygame.mouse.get_pos()[1] < 600:
                if not element_placed:
                    elements.append(current_item)
                    element_placed = True

        if element_placed and not pygame.mouse.get_pressed(3)[0]:
            element_placed = False

        if left_mouse_pressed and not pygame.mouse.get_pressed(3)[0]:
            left_mouse_pressed = False
            position_x += offset_x
            position_y += offset_y
            offset_x = 0
            offset_y = 0

        background.draw_background(screen, 40, position_x + offset_x, position_y + offset_y)

        if current_item is not None:
            element_position_x = -5 - position_x % 40 + (pygame.mouse.get_pos()[0] + position_x % 40) // 40 * 40
            element_position_y = -5 - position_y % 40 + (pygame.mouse.get_pos()[1] + position_y % 40) // 40 * 40
            image.set_alpha(127)
            screen.blit(image, pygame.Rect(pygame.Rect(element_position_x, element_position_y, image.get_rect()[2], image.get_rect()[3])))
            image.set_alpha(255)

        pygame.draw.rect(screen, Color(0, 0, 0), pygame.Rect(0, 596, 1200, 204), 6)
        pygame.draw.line(screen, Color(0, 0, 0), (0, 697), (599, 697), 6)
        for i in range(6):
            pygame.draw.line(screen, Color(0, 0, 0), (101 + 99 * i, 596), (101 + 99 * i, 800), 6)
        pygame.draw.line(screen, Color(0, 0, 0), (796, 596), (796, 800), 6)
        pygame.draw.line(screen, Color(0, 0, 0), (996, 596), (996, 800), 6)

        for toolbar_button in toolbar_buttons:
            button_state = toolbar_button.action()
            if button_state is not None:
                drag_ready = False
            if button_state is True:
                if current_item == toolbar_button.number:
                    current_item = None
                    image = None
                else:
                    current_item = toolbar_button.number
                    image = toolbar_button.image

        if show_info:
            drag_ready = False
            draw_info(screen, level)
            if okay.action():
                show_info = False

        if back.action():
            return None

        if level != 0:
            button_state = info.action()
            if button_state is not None:
                drag_ready = False
            if button_state is True:
                show_info = True

        button_state = start.action()
        if button_state is not None:
            drag_ready = False
        if button_state is True:
            print("start")

        button_state = stop.action()
        if button_state is not None:
            drag_ready = False
        if button_state is True:
            print("stop")

        button_state = step.action()
        if button_state is not None:
            drag_ready = False
        if button_state is True:
            print("step")

        if not drag_ready and not pygame.mouse.get_pressed(3)[0] and not show_info and ToolbarButton.which_pressed is None:
            drag_ready = True

        pygame.display.flip()
