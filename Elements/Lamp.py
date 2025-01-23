import pygame
import pygame.gfxdraw

class Lamp:
    def __init__(self, screen, pos_x, pos_y):
        self.image0 = pygame.image.load("Textures/Lampa0.png")
        self.image1 = pygame.image.load("Textures/Lampa1.png")
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.state = 0

    def draw(self, position_x, position_y):
        if self.state == 1:
            self.screen.blit(self.image1, pygame.Rect(self.pos_x * 40 - 5 - position_x, self.pos_y * 40 - 5 - position_y, 50, 50))
        else:
            self.screen.blit(self.image0, pygame.Rect(self.pos_x * 40 - 5 - position_x, self.pos_y * 40 - 5 - position_y, 50, 50))