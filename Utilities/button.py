import pygame
from pygame.locals import *

class Button:
    any_pressed = False

    def __init__(self, screen, text, font_path, pos_x, pos_y, width, height):
        self.screen = screen
        self.text = text
        self.font = pygame.font.Font(font_path, min(width * 2 // len(text), height * 2 // 3))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.pressed = False

    def draw(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height), border_radius=(min(self.height, self.width) // 10))
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.pos_x + self.width // 2 - text_surface.get_width() // 2, self.pos_y + self.height // 2 - text_surface.get_height() // 2))

    def action(self):
        if self.pressed:
            if pygame.mouse.get_pressed(3)[0]:
                self.draw(Color(230, 230, 230))
                return False
            else:
                self.draw(Color(230, 230, 230))
                self.pressed = False
                Button.any_pressed = False
                if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                    return True
                else:
                    return False

        if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
            if pygame.mouse.get_pressed(3)[0] and Button.any_pressed == False:
                self.pressed = True
                Button.any_pressed = True
                self.draw(Color(230, 230, 230))
                return False
            else:
                self.draw(Color(180, 180, 180))
        else:
            self.draw(Color(160, 160, 160))

        return None

class ToolbarButton:
    which_pressed = None
    which_marked = None

    def __init__(self, screen, image_path, pos_x, pos_y, width, height, number):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        if image_path == "Textures/Locked.png":
            self.locked = True
        else:
            self.locked = False
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.number = number

    def draw(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))
        self.screen.blit(self.image, pygame.Rect(self.pos_x + self.width // 2 - self.image.get_rect()[2] // 2, self.pos_y + self.height // 2 - self.image.get_rect()[3] // 2, self.width, self.height))

    def action(self):
        if self.locked:
            self.draw(Color(200, 200, 200))
            return None

        if ToolbarButton.which_marked == self.which_pressed == self.number:
            if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                if pygame.mouse.get_pressed(3)[0]:
                    self.draw(Color(120, 120, 120))
                else:
                    self.draw(Color(200, 200, 200))
                    ToolbarButton.which_marked = None
                    ToolbarButton.which_pressed = None
                    return True
            else:
                if pygame.mouse.get_pressed(3)[0]:
                    self.draw(Color(120, 120, 120))
                else:
                    self.draw(Color(150, 150, 150))
                    ToolbarButton.which_marked = None
        elif ToolbarButton.which_pressed is self.number:
            if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                if pygame.mouse.get_pressed(3)[0]:
                    self.draw(Color(120, 120, 120))
                    if ToolbarButton.which_marked is None:
                        ToolbarButton.which_marked = self.number
                    return False
                else:
                    self.draw(Color(160, 160, 160))
            else:
                if pygame.mouse.get_pressed(3)[0]:
                    self.draw(Color(150, 150, 150))
                else:
                    self.draw(Color(150, 150, 150))
        elif ToolbarButton.which_marked == self.number:
            if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                if pygame.mouse.get_pressed(3)[0]:
                    self.draw(Color(150, 150, 150))
                else:
                    self.draw(Color(150, 150, 150))
                    ToolbarButton.which_marked = None
                    ToolbarButton.which_pressed = self.number
                    return True
            else:
                if pygame.mouse.get_pressed(3)[0]:
                    self.draw(Color(150, 150, 150))
                else:
                    self.draw(Color(200, 200, 200))
                    ToolbarButton.which_marked = None
        else:
            if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                if pygame.mouse.get_pressed(3)[0] and ToolbarButton.which_marked is None:
                    self.draw(Color(150, 150, 150))
                    ToolbarButton.which_marked = self.number
                    return False
                else:
                    self.draw(Color(230, 230, 230))
            else:
                self.draw(Color(200, 200, 200))

        return None
