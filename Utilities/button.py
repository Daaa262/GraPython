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
        if self.pressed and pygame.mouse.get_pressed(3)[0]:
            self.draw(Color(230, 230, 230))
            return None
        elif self.pressed and not pygame.mouse.get_pressed(3)[0]:
            self.pressed = False
            Button.any_pressed = False
            if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                return True

        if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
            if pygame.mouse.get_pressed(3)[0] and Button.any_pressed == False:
                self.pressed = True
                Button.any_pressed = True
            else:
                self.draw(Color(180, 180, 180))
        else:
            self.draw(Color(160, 160, 160))

class ToolbarButton:
    any_pressed = False

    def __init__(self, screen, image_path, pos_x, pos_y, width, height, number):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.pressed = False

    def draw(self, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))
        self.screen.blit(self.image, pygame.Rect(self.pos_x + self.width // 2 - self.image.get_rect()[2] // 2, self.pos_y + self.height // 2 - self.image.get_rect()[3] // 2, self.width, self.height))

    def action(self):
        if self.pressed and pygame.mouse.get_pressed(3)[0]:
            self.draw(Color(160, 160, 160))
            return None
        elif self.pressed and not pygame.mouse.get_pressed(3)[0]:
            self.pressed = False
            ToolbarButton.any_pressed = False
            if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
                return True

        if self.pos_x <= pygame.mouse.get_pos()[0] <= self.pos_x + self.width and self.pos_y <= pygame.mouse.get_pos()[1] <= self.pos_y + self.height:
            if pygame.mouse.get_pressed(3)[0] and ToolbarButton.any_pressed == False:
                self.pressed = True
                ToolbarButton.any_pressed = True
            else:
                self.draw(Color(230, 230, 230))
        else:
            self.draw(Color(200, 200, 200))