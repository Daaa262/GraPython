import pygame
from pygame.locals import *

import Elements.Source
from Utilities import background
import Utilities.button
from Levels.Info import draw_info
from Utilities.button import ToolbarButton
from Elements import Wire, Lamp, Source, Transmitter, Transistor

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
    element_update = False

    something_clicked = False

    start_wire = False
    start_wire_x = 0
    start_wire_y = 0
    element_connected = None
    joint_connected = None

    wires = []

    run_simulation = False
    last_step = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_TAB and left_mouse_pressed is False:
                    position_x = 0
                    position_y = 0

        if pygame.mouse.get_pressed(3)[0] and pygame.mouse.get_pos()[1] < 600:
            if current_item is not None:
                if not element_update:
                    new_element_position = (pygame.mouse.get_pos()[0] + position_x) // 40, (pygame.mouse.get_pos()[1] + position_y) // 40
                    if current_item != 0:
                        element_can_be_placed = True
                        for element in elements:
                            if abs(element.pos_x - new_element_position[0]) <= 2 and abs(element.pos_y - new_element_position[1]) <= 2:
                                element_can_be_placed = False
                                break
                        if element_can_be_placed:
                            if current_item == 1:
                                elements.append(Lamp.Lamp(screen, *new_element_position))
                            elif current_item == 2:
                                elements.append(Source.Source(screen, *new_element_position))
                            elif current_item == 3:
                                elements.append(Transmitter.Transmitter(screen, *new_element_position))
                            elif current_item == 4:
                                elements.append(Transistor.Transistor(screen, *new_element_position))
                            element_update = True
                    else:
                        for element in elements:
                            if element.pos_x == new_element_position[0] and element.pos_y == new_element_position[1]:
                                wire_to_delete = []
                                for wire in element.wires_connected:
                                    wire_to_delete.append(wire)
                                for wire in wire_to_delete:
                                    wire.element1.wires_connected.remove(wire)
                                    wire.element2.wires_connected.remove(wire)
                                    wires.remove(wire)
                                elements.remove(element)
                                element_update = True
                                break
            elif not something_clicked:
                for element in elements:
                    if element.clicked(pygame.mouse.get_pos()[0] + position_x + offset_x , pygame.mouse.get_pos()[1] + position_y + offset_y) is not None:
                        if element is element_connected:
                            break
                        if start_wire:
                            wires.append(Elements.Wire.Wire(start_wire_x, start_wire_y, element_connected, joint_connected, *element.clicked(pygame.mouse.get_pos()[0] + position_x + offset_x , pygame.mouse.get_pos()[1] + position_y + offset_y)))
                            element.wires_connected.append(wires[-1])
                            element_connected.wires_connected.append(wires[-1])
                            element_connected = None
                            start_wire = False
                            something_clicked = True
                            break
                        else:
                            start_wire_x, start_wire_y, element_connected, joint_connected = element.clicked(pygame.mouse.get_pos()[0] + position_x + offset_x , pygame.mouse.get_pos()[1] + position_y + offset_y)
                            start_wire = True
                            break
                if not start_wire and not something_clicked:
                    for element in elements:
                        if type(element) is Elements.Source.Source:
                            if element.pos_x * 40 - 5 < pygame.mouse.get_pos()[0] + position_x + offset_x < element.pos_x * 40 + 45 and element.pos_y * 40 - 5 < pygame.mouse.get_pos()[1] + position_y + offset_y < element.pos_y * 40 + 45:
                                element.state[0] = (element.state[0] + 1) % 2
                                element.state[1] = (element.state[1] + 1) % 2
                                element.state[2] = (element.state[2] + 1) % 2
                                element.state[3] = (element.state[3] + 1) % 2
                                something_clicked = True
            if drag_ready is True and not something_clicked:
                if not left_mouse_pressed:
                    left_mouse_pressed = True
                    pressed_x, pressed_y = pygame.mouse.get_pos()
                else:
                    offset_x, offset_y = pressed_x - pygame.mouse.get_pos()[0], pressed_y - pygame.mouse.get_pos()[1]

        if element_update and not pygame.mouse.get_pressed(3)[0]:
            element_update = False

        if left_mouse_pressed and not pygame.mouse.get_pressed(3)[0]:
            left_mouse_pressed = False
            position_x += offset_x
            position_y += offset_y
            offset_x = 0
            offset_y = 0

        if something_clicked and not pygame.mouse.get_pressed(3)[0]:
            something_clicked = False

        background.draw_background(screen, 40, position_x + offset_x, position_y + offset_y)

        for element in elements:
            element.draw(position_x + offset_x, position_y + offset_y)

        if current_item is not None:
            if pygame.mouse.get_pressed(3)[2]:
                current_item = None
                ToolbarButton.which_marked = None
                ToolbarButton.which_pressed = None
            if current_item == 0:
                for element in elements:
                    if element.pos_x == (pygame.mouse.get_pos()[0] + position_x) // 40 and element.pos_y == (pygame.mouse.get_pos()[1] + position_y) // 40:
                        element_position_x = (40 - image.get_rect()[2]) // 2 - position_x % 40 + (pygame.mouse.get_pos()[0] + position_x % 40) // 40 * 40
                        element_position_y = (40 - image.get_rect()[3]) // 2 - position_y % 40 + (pygame.mouse.get_pos()[1] + position_y % 40) // 40 * 40
                        screen.blit(image, pygame.Rect(pygame.Rect(element_position_x, element_position_y, image.get_rect()[2], image.get_rect()[3])))
                        break
            elif elements:
                draw_transparent = False
                for element in elements:
                    if abs(element.pos_x - (pygame.mouse.get_pos()[0] + position_x) // 40) <= 2 and abs(element.pos_y - (pygame.mouse.get_pos()[1] + position_y) // 40) <= 2:
                        draw_transparent = True
                        break
                if draw_transparent:
                    image.set_alpha(70)
                else:
                    image.set_alpha(190)
                element_position_x = (40 - image.get_rect()[2]) // 2 - position_x % 40 + (pygame.mouse.get_pos()[0] + position_x % 40) // 40 * 40
                element_position_y = (40 - image.get_rect()[3]) // 2 - position_y % 40 + (pygame.mouse.get_pos()[1] + position_y % 40) // 40 * 40
                screen.blit(image, pygame.Rect(pygame.Rect(element_position_x, element_position_y, image.get_rect()[2], image.get_rect()[3])))
                image.set_alpha(255)
            else:
                element_position_x = (40 - image.get_rect()[2]) // 2 - position_x % 40 + (pygame.mouse.get_pos()[0] + position_x % 40) // 40 * 40
                element_position_y = (40 - image.get_rect()[3]) // 2 - position_y % 40 + (pygame.mouse.get_pos()[1] + position_y % 40) // 40 * 40
                image.set_alpha(190)
                screen.blit(image, pygame.Rect(pygame.Rect(element_position_x, element_position_y, image.get_rect()[2], image.get_rect()[3])))
                image.set_alpha(255)

        for wire in wires:
            if wire.powered:
                pygame.draw.line(screen, Color(0, 210, 0), (wire.pos_x1 - position_x - offset_x, wire.pos_y1 - position_y - offset_y), (wire.pos_x2 - position_x - offset_x, wire.pos_y2 - position_y - offset_y), width=3)
            else:
                pygame.draw.line(screen, Color(0, 0, 0), (wire.pos_x1 - position_x - offset_x, wire.pos_y1 - position_y - offset_y), (wire.pos_x2 - position_x - offset_x, wire.pos_y2 - position_y - offset_y), width=3)

        if start_wire:
            pygame.draw.line(screen, Color(0, 0, 0), (start_wire_x - position_x - offset_x, start_wire_y - position_y - offset_y), pygame.mouse.get_pos(), width=3)
            if pygame.mouse.get_pressed(3)[2]:
                element_connected = None
                start_wire = False

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

        button_state = back.action()
        if button_state is not None:
            drag_ready = False
        if button_state is True:
            ToolbarButton.which_pressed = None
            ToolbarButton.which_marked = None
            return None

        if level != 0:
            button_state = info.action()
            if button_state is not None:
                drag_ready = False
            if button_state is True:
                show_info = True

        if run_simulation:
            if pygame.time.get_ticks() - last_step > 100:
                last_step = pygame.time.get_ticks()
                for element in elements:
                    element.read_input()
                for wire in wires:
                    wire.powered = False
                for element in elements:
                    element.set_output()

        if not run_simulation:
            button_state = start.action()
            if button_state is not None:
                drag_ready = False
            if button_state is True:
                last_step = pygame.time.get_ticks()
                run_simulation = True

        if run_simulation:
            button_state = stop.action()
            if button_state is not None:
                drag_ready = False
            if button_state is True:
                run_simulation = False

        if not run_simulation:
            button_state = step.action()
            if button_state is not None:
                drag_ready = False
            if button_state is True:
                for element in elements:
                    element.read_input()
                for wire in wires:
                    wire.powered = False
                for element in elements:
                    element.set_output()

        if not drag_ready and not pygame.mouse.get_pressed(3)[0] and not show_info and ToolbarButton.which_pressed is None:
            drag_ready = True

        pygame.display.flip()
