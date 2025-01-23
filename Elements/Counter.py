import pygame
import pygame.gfxdraw

class Counter:
    def __init__(self, screen, pos_x, pos_y):
        self.image = pygame.image.load("Textures/Licznik.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [0] * 9
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []
        self.change = False

    def clicked(self, position_x, position_y):
        for i in range(8):
            if self.pos_x * 40 - 30 + 12 * i < position_x < self.pos_x * 40 - 30 + 12 * i + 15 and self.pos_y * 40 - 5 - 7 < position_y < self.pos_y * 40 - 5 + 8:
                return self.pos_x * 40 - 30 + 12 * i + 7, self.pos_y * 40 - 5, self, i
        if self.pos_x * 40 - 30 + 43 < position_x < self.pos_x * 40 - 30 + 58 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
            return self.pos_x * 40 - 30 + 50, self.pos_y * 40 - 5 + 50, self, 8
        return None

    def read_input(self):
        for wire in self.wires_connected:
            if wire.powered:
                if wire.element1 == self and wire.joint1 == 8 or wire.element2 == self and wire.joint2 == 8:
                    if self.state[8] == 0:
                        self.change = True
                    self.state[8] = 1
                    return None
        self.state[8] = 0

    def set_output(self):
        if self.change:
            self.change = False
            for i in range(8):
                if self.state[i] == 0:
                    self.state[i] = 1
                    break
                else:
                    self.state[i] = 0

        for i in range(8):
            for wire in self.wires_connected:
                if (wire.element1 == self and wire.joint1 == i or wire.element2 == self and wire.joint2 == i) and self.state[i] == 1:
                    wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 30 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        self.screen.blit(self.image, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        for i in range(8):
            if self.state[i] == 1:
                self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 12 * i, on_screen_y - 7, 15, 15))
            else:
                self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 12 * i, on_screen_y - 7, 15, 15))
        if self.state[8] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 43, on_screen_y + 43, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 43, on_screen_y + 43, 15, 15))