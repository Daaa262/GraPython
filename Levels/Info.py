import pygame
from pygame.locals import *

pygame.font.init()
font = pygame.font.Font("Fonts/Manolo.ttf", 40)

def draw_info(screen, level):
    pygame.draw.rect(screen, Color(140, 140, 140), pygame.Rect(200, 100, 800, 600), border_radius=40)

    if level == 1:
        text_surface = font.render("1.Kliknij prawym przyciskiem", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("na zrodlo zasilania,aby", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render("zapalic lampe.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))
    elif level == 2:
        text_surface = font.render("2.Polacz lampe ze zrodlem", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("zasilania i ja zapal.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
    elif level == 3:
        text_surface = font.render("3.Zapal trzy lampy za pomoca", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("zrodla zasilania.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
    elif level == 4:
        text_surface = font.render("4.Zbuduj bramke OR.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
    elif level == 5:
        text_surface = font.render("5.Zbuduj bramke NOT.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
    elif level == 6:
        text_surface = font.render("6.Zbuduj zegar,ktory zmienia", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("stan co 1 krok.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
    elif level == 7:
        text_surface = font.render("7.Zbuduj bramke AND.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
    elif level == 8:
        text_surface = font.render("8.Zbuduj element,ktory", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("zmienia stan wyjscia", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render("za kazdym razem,gdy na", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))
        text_surface = font.render("wejsciu pojawi sie sygnal.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 300))
    elif level == 9:
        text_surface = font.render("9.Zbuduj bramke XOR.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
    elif level == 10:
        text_surface = font.render("10.Zbuduj pelny sumator.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
    elif level == 11:
        text_surface = font.render("11.Zbuduj zegar na ktorym", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("mozna ustawic czestotliwosc", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render("odpowiednio 1,2 i 4 kroki.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))
    elif level == 12:
        text_surface = font.render("12.Zbuduj sumator dwoch", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render( "liczb binarnych osmio", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render( "bitowych.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))
    elif level == 13:
        text_surface = font.render("13.Zbuduj licznik,ktory", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("zwieksza liczbe na wyjsciu", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render("za kazdym razem,gdy na", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))
        text_surface = font.render("wejsciu pojawi sie sygnal.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 300))
    elif level == 14:
        text_surface = font.render("14.Zbuduj uklad ktory ma trzy", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("wejscia dwu bitowe i jedno", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render("wejscie, ktore wybiera ktory", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))
        text_surface = font.render("sygnal pojawi sie na wyjsciu.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 300))
    elif level == 15:
        text_surface = font.render("15.Zbuduj uklad,ktory mnozy", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("trzy bitowe liczby binarne.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
    elif level == 16:
        text_surface = font.render("16.Zbuduj uklad,ktory dzieli", True, (0, 0, 0))
        screen.blit(text_surface, (250, 150))
        text_surface = font.render("liczby 6 bitowe i podaje", True, (0, 0, 0))
        screen.blit(text_surface, (250, 200))
        text_surface = font.render("wynik oraz reszte.", True, (0, 0, 0))
        screen.blit(text_surface, (250, 250))