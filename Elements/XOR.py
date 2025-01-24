import pygame
import pygame.gfxdraw

class XOR:
    def __init__(self, screen, pos_x, pos_y, deletable):
        self.image = pygame.image.load("Textures/XOR.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [0, 0, 0]
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []
        self.deletable = deletable

    def clicked(self, position_x, position_y):
        if self.pos_x * 40 - 5 + 17 < position_x < self.pos_x * 40 - 5 + 32 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
            return self.pos_x * 40 - 5 + 25, self.pos_y * 40 - 5, self, 2
        if self.pos_x * 40 - 5 + 35 < position_x < self.pos_x * 40 - 5 + 50 and self.pos_y * 40 - 5 + 40 < position_y < self.pos_y * 40 - 5 + 55:
            return self.pos_x * 40 - 5 + 42, self.pos_y * 40 - 5 + 47, self, 1
        elif self.pos_x * 40 - 5 < position_x < self.pos_x * 40 - 5 + 15 and self.pos_y * 40 - 5 + 40 < position_y < self.pos_y * 40 - 5 + 55:
            return self.pos_x * 40 - 5 + 7, self.pos_y * 40 - 5 + 47, self, 0
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
        if self.state[0] != self.state[1]:
            self.state[2] = 1
            for wire in self.wires_connected:
                if wire.element1 == self and wire.joint1 == 2 or wire.element2 == self and wire.joint2 == 2:
                    wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 5 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        self.screen.blit(self.image, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        if self.state[0] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x, on_screen_y + 40, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x, on_screen_y + 40, 15, 15))
        if self.state[1] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 35, on_screen_y + 40, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 35, on_screen_y + 40, 15, 15))
        if self.state[2] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 18, on_screen_y - 8, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 18, on_screen_y - 8, 15, 15))