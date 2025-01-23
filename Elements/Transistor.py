import pygame
import pygame.gfxdraw

class Transistor:
    def __init__(self, screen, pos_x, pos_y):
        self.image000 = pygame.image.load("Textures/Tranzystor000.png")
        self.image001 = pygame.image.load("Textures/Tranzystor001.png")
        self.image010 = pygame.image.load("Textures/Tranzystor010.png")
        self.image011 = pygame.image.load("Textures/Tranzystor011.png")
        self.image100 = pygame.image.load("Textures/Tranzystor100.png")
        self.image101 = pygame.image.load("Textures/Tranzystor101.png")
        self.image110 = pygame.image.load("Textures/Tranzystor110.png")
        self.image111 = pygame.image.load("Textures/Tranzystor111.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [0, 0, 0]
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []

    def clicked(self, position_x, position_y):
        if self.pos_x * 40 - 5 + 17 < position_x < self.pos_x * 40 - 5 + 32 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
            return self.pos_x * 40 - 5 + 24, self.pos_y * 40 - 5, self, 2
        if self.pos_x * 40 - 5 + 43 < position_x < self.pos_x * 40 - 5 + 58 and self.pos_y * 40 - 5 + 18 < position_y < self.pos_y * 40 - 5 + 33:
            return self.pos_x * 40 - 5 + 50, self.pos_y * 40 - 5 + 25, self, 1
        elif self.pos_x * 40 - 5 + 18 < position_x < self.pos_x * 40 - 5 + 33 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
            return self.pos_x * 40 - 5 + 25, self.pos_y * 40 - 5 + 50, self, 0
        else:
            return None

    def read_input(self):
        self.state = [0, 0, 0]
        for wire in self.wires_connected:
            if wire.powered:
                if wire.element1 == self and wire.joint1 == 0 or wire.element2 == self and wire.joint2 == 0:
                    self.state[0] = 1
                if wire.element1 == self and wire.joint1 == 1 or wire.element2 == self and wire.joint2 == 1:
                    self.state[1] = 1

    def set_output(self):
        if self.state[0] == 1 and self.state[1] == 0:
            self.state[2] = 1
            for wire in self.wires_connected:
                if wire.element1 == self and wire.joint1 == 2 or wire.element2 == self and wire.joint2 == 2:
                    wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 5 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        if self.state == [0, 0, 0]:
            self.screen.blit(self.image000, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [1, 0, 0]:
            self.screen.blit(self.image001, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [0, 1, 0]:
            self.screen.blit(self.image010, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [1, 1, 0]:
            self.screen.blit(self.image011, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [0, 0, 1]:
            self.screen.blit(self.image100, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [1, 0, 1]:
            self.screen.blit(self.image101, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [0, 1, 1]:
            self.screen.blit(self.image110, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        elif self.state == [1, 1, 1]:
            self.screen.blit(self.image111, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        if self.state[0] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 18, on_screen_y + 43, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 18, on_screen_y + 43, 15, 15))
        if self.state[1] == 1:
            self.screen.blit(pygame.transform.rotate(self.joint1, 90), pygame.Rect(on_screen_x + 43, on_screen_y + 18, 15, 15))
        else:
            self.screen.blit(pygame.transform.rotate(self.joint0, 90), pygame.Rect(on_screen_x + 43, on_screen_y + 18, 15, 15))
        if self.state[2] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 17, on_screen_y - 8, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 17, on_screen_y - 8, 15, 15))