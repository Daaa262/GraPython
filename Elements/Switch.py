import pygame
import pygame.gfxdraw

class Switch:
    def __init__(self, screen, pos_x, pos_y, deletable):
        self.image = pygame.image.load("Textures/Włącznik.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [0, 0]
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []
        self.change = False
        self.deletable = deletable

    def clicked(self, position_x, position_y):
        if self.pos_x * 40 - 5 + 17 < position_x < self.pos_x * 40 - 5 + 32 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
            return self.pos_x * 40 - 5 + 25, self.pos_y * 40 - 5, self, 1
        elif self.pos_x * 40 - 5 + 18 < position_x < self.pos_x * 40 - 5 + 33 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
            return self.pos_x * 40 - 5 + 25, self.pos_y * 40 - 5 + 50, self, 0
        else:
            return None

    def read_input(self):
        for wire in self.wires_connected:
            if wire.powered:
                if wire.element1 == self and wire.joint1 == 0 or wire.element2 == self and wire.joint2 == 0:
                    if self.state[0] == 0:
                        self.change = True
                    self.state[0] = 1
                    return None
        self.state[0] = 0

    def set_output(self):
        if self.change:
            self.change = False
            self.state[1] = (self.state[1] + 1) % 2

        if self.state[1] == 1:
            for wire in self.wires_connected:
                if wire.element1 == self and wire.joint1 == 1 or wire.element2 == self and wire.joint2 == 1:
                    wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 5 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        self.screen.blit(self.image, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        if self.state[0] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 18, on_screen_y + 43, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 18, on_screen_y + 43, 15, 15))
        if self.state[1] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 17, on_screen_y - 8, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 17, on_screen_y - 8, 15, 15))