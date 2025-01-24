import pygame
import pygame.gfxdraw

class Adder:
    def __init__(self, screen, pos_x, pos_y, deletable):
        self.image = pygame.image.load("Textures/Sumator.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [0, 0, 0, 0, 0]
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []
        self.deletable = deletable

    def clicked(self, position_x, position_y):
        if self.pos_x * 40 - 5 + 6 < position_x < self.pos_x * 40 - 5 + 21 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
            return self.pos_x * 40 - 5 + 13, self.pos_y * 40 - 5 + 50, self, 0
        elif self.pos_x * 40 - 5 + 30 < position_x < self.pos_x * 40 - 5 + 45 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
            return self.pos_x * 40 - 5 + 37, self.pos_y * 40 - 5 + 50, self, 1
        if self.pos_x * 40 - 5 + 43 < position_x < self.pos_x * 40 - 5 + 58 and self.pos_y * 40 - 5 + 18 < position_y < self.pos_y * 40 - 5 + 33:
            return self.pos_x * 40 - 5 + 50, self.pos_y * 40 - 5 + 25, self, 2
        if self.pos_x * 40 - 5 + 6 < position_x < self.pos_x * 40 - 5 + 21 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
            return self.pos_x * 40 - 5 + 13, self.pos_y * 40 - 5, self, 3
        elif self.pos_x * 40 - 5 + 30 < position_x < self.pos_x * 40 - 5 + 45 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
            return self.pos_x * 40 - 5 + 37, self.pos_y * 40 - 5, self, 4
        else:
            return None

    def read_input(self):
        self.state = [0, 0, 0, 0, 0]
        for wire in self.wires_connected:
            if wire.powered:
                if wire.element1 == self and wire.joint1 == 0 or wire.element2 == self and wire.joint2 == 0:
                    self.state[0] = 1
                if wire.element1 == self and wire.joint1 == 1 or wire.element2 == self and wire.joint2 == 1:
                    self.state[1] = 1
                if wire.element1 == self and wire.joint1 == 2 or wire.element2 == self and wire.joint2 == 2:
                    self.state[2] = 1

    def set_output(self):
        if self.state[0] + self.state[1] + self.state[2] == 3:
            self.state[3] = 1
            self.state[4] = 1
        elif self.state[0] + self.state[1] + self.state[2] == 2:
            self.state[3] = 1
        elif self.state[0] + self.state[1] + self.state[2] == 1:
            self.state[4] = 1
        for wire in self.wires_connected:
            if (wire.element1 == self and wire.joint1 == 3 or wire.element2 == self and wire.joint2 == 3) and self.state[3] == 1:
                wire.powered = True
            if (wire.element1 == self and wire.joint1 == 4 or wire.element2 == self and wire.joint2 == 4) and self.state[4] == 1:
                wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 5 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        self.screen.blit(self.image, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
        if self.state[0] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 6, on_screen_y + 43, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 6, on_screen_y + 43, 15, 15))
        if self.state[1] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 30, on_screen_y + 43, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 30, on_screen_y + 43, 15, 15))
        if self.state[2] == 1:
            self.screen.blit(pygame.transform.rotate(self.joint1, 90), pygame.Rect(on_screen_x + 43, on_screen_y + 18, 15, 15))
        else:
            self.screen.blit(pygame.transform.rotate(self.joint0, 90), pygame.Rect(on_screen_x + 43, on_screen_y + 18, 15, 15))
        if self.state[3] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 6, on_screen_y - 8, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 6, on_screen_y - 8, 15, 15))
        if self.state[4] == 1:
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 30, on_screen_y - 8, 15, 15))
        else:
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 30, on_screen_y - 8, 15, 15))