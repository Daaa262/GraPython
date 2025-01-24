import pygame
import pygame.gfxdraw

class Source:
    def __init__(self, screen, pos_x, pos_y, deletable):
        self.image0 = pygame.image.load("Textures/Źródło0.png")
        self.image1 = pygame.image.load("Textures/Źródło1.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = [1, 1, 1, 1]
        self.joint0 = pygame.image.load("Textures/Złącze0.png")
        self.joint1 = pygame.image.load("Textures/Złącze1.png")
        self.wires_connected = []
        self.deletable = deletable

    def clicked(self, position_x, position_y):
        if self.pos_x * 40 - 5 + 17 < position_x < self.pos_x * 40 - 5 + 32 and self.pos_y * 40 - 5 - 8 < position_y < self.pos_y * 40 - 5 + 7:
            return self.pos_x * 40 - 5 + 25, self.pos_y * 40 - 5, self, 0
        elif self.pos_x * 40 - 5 - 8 < position_x < self.pos_x * 40 - 5 + 7 and self.pos_y * 40 - 5 + 17 < position_y < self.pos_y * 40 - 5 + 32:
            return self.pos_x * 40 - 5, self.pos_y * 40 - 5 + 25, self, 1
        elif self.pos_x * 40 - 5 + 18 < position_x < self.pos_x * 40 - 5 + 33 and self.pos_y * 40 - 5 + 43 < position_y < self.pos_y * 40 - 5 + 58:
            return self.pos_x * 40 - 5 + 25, self.pos_y * 40 - 5 + 50, self, 2
        elif self.pos_x * 40 - 5 + 43 < position_x < self.pos_x * 40 - 5 + 58 and self.pos_y * 40 - 5 + 18 < position_y < self.pos_y * 40 - 5 + 33:
            return self.pos_x * 40 - 5 + 50, self.pos_y * 40 - 5 + 25, self, 3
        else:
            return None

    def read_input(self):
        return None

    def set_output(self):
        if self.state == [1, 1, 1, 1]:
            for wire in self.wires_connected:
                wire.powered = True

    def draw(self, position_x, position_y):
        on_screen_x = self.pos_x * 40 - 5 - position_x
        on_screen_y = self.pos_y * 40 - 5 - position_y
        if self.state == [1, 1, 1, 1]:
            self.screen.blit(self.image1, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
            self.screen.blit(self.joint1, pygame.Rect(on_screen_x + 17, on_screen_y - 8, 15, 15))
            self.screen.blit(pygame.transform.rotate(self.joint1, 90), pygame.Rect(on_screen_x - 8, on_screen_y + 17, 15, 15))
            self.screen.blit(pygame.transform.rotate(self.joint1, 180), pygame.Rect(on_screen_x + 18, on_screen_y + 43, 15, 15))
            self.screen.blit(pygame.transform.rotate(self.joint1, 270), pygame.Rect(on_screen_x + 43, on_screen_y + 18, 15, 15))
        else:
            self.screen.blit(self.image0, pygame.Rect(on_screen_x, on_screen_y, 50, 50))
            self.screen.blit(self.joint0, pygame.Rect(on_screen_x + 17, on_screen_y - 8, 15, 15))
            self.screen.blit(pygame.transform.rotate(self.joint0, 90), pygame.Rect(on_screen_x - 8, on_screen_y + 17, 15, 15))
            self.screen.blit(pygame.transform.rotate(self.joint0, 180), pygame.Rect(on_screen_x + 18, on_screen_y + 43, 15, 15))
            self.screen.blit(pygame.transform.rotate(self.joint0, 270), pygame.Rect(on_screen_x + 43, on_screen_y + 18, 15, 15))