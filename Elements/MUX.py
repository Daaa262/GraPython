import pygame
import pygame.gfxdraw

class MUX:
    def __init__(self, screen, pos_x, pos_y):
        self.image = pygame.image.load("Textures/Multiplekser.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [0] * 13
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []

    def clicked(self, position_x, position_y):
        for i in range(4):
            if self.pos_x * 40 - 30 - 4 + 12 * i < position_x < self.pos_x * 40 - 30 - 4 + 12 * i + 15 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
                return self.pos_x * 40 - 30 - 4 + 12 * i + 7, self.pos_y * 40 - 5 + 50, self, i
            if self.pos_x * 40 - 30 + 54 + 12 * i < position_x < self.pos_x * 40 - 30 + 54 + 12 * i + 15 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
                return self.pos_x * 40 - 30 + 54 + 12 * i + 7, self.pos_y * 40 - 5 + 50, self, i + 4
            if self.pos_x * 40 - 30 + 18 + 16 * i < position_x < self.pos_x * 40 - 30 + 18 + 16 * i + 15 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
                return self.pos_x * 40 - 30 + 18 + 16 * i + 7, self.pos_y * 40 - 5, self, i + 8
        if self.pos_x * 40 - 30 + 93 < position_x < self.pos_x * 40 - 30 + 108 and self.pos_y * 40 - 5 + 16 < position_y < self.pos_y * 40 - 5 + 31:
            return self.pos_x * 40 - 30 + 100, self.pos_y * 40 - 5 + 23, self, 12
        return None

    def read_input(self):
        self.state = [0] * 13
        for wire in self.wires_connected:
            if wire.powered:
                for i in range(8):
                    if wire.element1 == self and wire.joint1 == i or wire.element2 == self and wire.joint2 == i:
                        self.state[i] = 1
                if wire.element1 == self and wire.joint1 == 12 or wire.element2 == self and wire.joint2 == 12:
                    self.state[12] = 1

    def set_output(self):
        if self.state[12] == 1:
            for i in range(4):
                self.state[i + 8] = self.state[i + 4]
        else:
            for i in range(4):
                self.state[i + 8] = self.state[i]
        for i in range(4):
            for wire in self.wires_connected:
                if (wire.element1 == self and wire.joint1 == i + 8 or wire.element2 == self and wire.joint2 == i + 8) and self.state[i + 8] == 1:
                    wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 30 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        self.screen.blit(self.image, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        for i in range(4):
            if self.state[i] == 1:
                self.screen.blit(self.joint1, pygame.Rect(on_screen_x - 4 + 12 * i, on_screen_y + 43, 15, 15))
            else:
                self.screen.blit(self.joint0, pygame.Rect(on_screen_x - 4 + 12 * i, on_screen_y + 43, 15, 15))
            if self.state[i + 4] == 1:
                self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 54 + 12 * i, on_screen_y + 43, 15, 15))
            else:
                self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 54 + 12 * i, on_screen_y + 43, 15, 15))
        for i in range(4):
            if self.state[i + 8] == 1:
                self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 18 + 16 * i, on_screen_y - 8, 15, 15))
            else:
                self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 18 + 16 * i, on_screen_y - 8, 15, 15))
        if self.state[12] == 1:
            self.screen.blit(pygame.transform.rotate(self.joint1, 90), pygame.Rect(on_screen_x + 93, on_screen_y + 16, 15, 15))
        else:
            self.screen.blit(pygame.transform.rotate(self.joint0, 90), pygame.Rect(on_screen_x + 93, on_screen_y + 16, 15, 15))