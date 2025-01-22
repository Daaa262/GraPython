import pygame
from pygame.locals import *
import game
import Utilities.button
import levelselect
from Utilities.background import draw_background

pygame.font.init()

def go(screen):
    button1 = Utilities.button.Button(screen, "Tryb Fabularny", "Fonts/Manolo.ttf", 350, 350, 500, 70)
    button2 = Utilities.button.Button(screen, "Sandbox", "Fonts/Manolo.ttf", 350, 450, 500, 70)
    button3 = Utilities.button.Button(screen, "Koniec", "Fonts/Manolo.ttf", 350, 550, 500, 70)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        draw_background(screen, 40)

        if button1.action():
            levelselect.go(screen)
        if button2.action():
            game.go(screen, 0)
        if button3.action():
            return None

        pygame.display.flip()
