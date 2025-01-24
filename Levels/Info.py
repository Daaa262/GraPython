import pygame
from pygame.locals import *
from Elements import Wire, Lamp, Source, Transmitter, Transistor, Single, NOT, AND, Clock, Switch, XOR, Adder, BigAdder, Counter, MUX

pygame.font.init()
font = pygame.font.Font("Fonts/Manolo.ttf", 40)

def draw_info(screen, level):
    pygame.draw.rect(screen, Color(140, 140, 140), pygame.Rect(200, 100, 800, 600), border_radius=40)

    if level == 1:
        text_surface = font.render("1.Kliknij lewym przyciskiem", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("na zrodlo zasilania,aby", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("zapalic lampe. Przyciski po", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
        text_surface = font.render("prawej stronie aktualizuja", True, (0, 0, 0))
        screen.blit(text_surface, (240, 300))
        text_surface = font.render("stan symulacji.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 350))
    elif level == 2:
        text_surface = font.render("2.Polacz lampe ze zrodlem", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("zasilania i ja zapal.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
    elif level == 3:
        text_surface = font.render("3.Zapal trzy lampy za pomoca", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("zrodla zasilania.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
    elif level == 4:
        text_surface = font.render("4.Umiesc zrodlo zasilania", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("oraz lampe,a nastepnie", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("ja zapal.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
    elif level == 5:
        text_surface = font.render("5.Zbuduj bramke OR.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
    elif level == 6:
        text_surface = font.render("6.Zbuduj bramke NOT.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
    elif level == 7:
        text_surface = font.render("7.Zbuduj bramke AND.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
    elif level == 8:
        text_surface = font.render("8.Zbuduj element,ktory", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("zapala lampe na jeden", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("krok gdy dostanie sygnal.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
    elif level == 9:
        text_surface = font.render("9.Zbuduj zegar,ktory zmienia", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("stan lampy co 2 kroki.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("Przycisk \"start\" wykonuje", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
        text_surface = font.render("kroki automatycznie.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 300))
    elif level == 10:
        text_surface = font.render("10.Zbuduj element,ktory", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("zapala lampe tylko,gdy", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("dostanie sygnal 10110.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
    elif level == 11:
        text_surface = font.render("11. Zbuduj bramke XOR.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
    elif level == 12:
        text_surface = font.render("12.Zbuduj uklad ktory ma dwa", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("wejscia cztero bitowe i jedno", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("wejscie, ktore wybiera ktory", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
        text_surface = font.render("sygnal pojawi sie na wyjsciu.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 300))
    elif level == 13:
        text_surface = font.render("13.Zbuduj pelny sumator.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
    elif level == 14:
        text_surface = font.render("14.Zbuduj sumator dwoch", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render( "liczb cztero bitowych.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
    elif level == 15:
        text_surface = font.render("15.Zbuduj uklad,ktory mnozy", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("trzy bitowe liczby binarne.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
    elif level == 16:
        text_surface = font.render("16.Zbuduj element,ktory", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("zmienia stan wyjscia", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("za kazdym razem,gdy na", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
        text_surface = font.render("wejsciu pojawi sie sygnal.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 300))
    elif level == 17:
        text_surface = font.render("17.Zbuduj licznik,ktory", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("zwieksza liczbe na wyjsciu", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("za kazdym razem,gdy na", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
        text_surface = font.render("wejsciu pojawi sie sygnal.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 300))
    elif level == 18:
        text_surface = font.render("18.Zbuduj uklad,ktory dzieli", True, (0, 0, 0))
        screen.blit(text_surface, (240, 150))
        text_surface = font.render("liczby cztero bitowe i podaje", True, (0, 0, 0))
        screen.blit(text_surface, (240, 200))
        text_surface = font.render("wynik oraz reszte z dzielenia.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 250))
        text_surface = font.render("W przypadku dzielenia przez", True, (0, 0, 0))
        screen.blit(text_surface, (240, 300))
        text_surface = font.render("zero na wyjsciu sa same zera.", True, (0, 0, 0))
        screen.blit(text_surface, (240, 350))

def availability(level):
    if level == 0:
        return [-1] * 14
    elif level == 4:
        return [1, 1] + [0] * 12
    else:
        return [0] * 14

def check_conditions(level, elements):
    if level == 1:
        if elements[1].state[2] == 1:
            return True
    elif level == 2:
        if elements[1].state[0] == 1 or elements[1].state[1] == 1 or elements[1].state[2] == 1 or elements[1].state[3] == 1:
            return True
    elif level == 3:
        if (elements[1].state[0] == 1 or elements[1].state[1] == 1 or elements[1].state[2] == 1 or elements[1].state[3] == 1) and (elements[2].state[0] == 1 or elements[2].state[1] == 1 or elements[2].state[2] == 1 or elements[2].state[3] == 1) and (elements[3].state[0] == 1 or elements[3].state[1] == 1 or elements[3].state[2] == 1 or elements[3].state[3] == 1):
            return True
    elif level == 4:
        if len(elements) == 2:
            if type(elements[0]) == Lamp.Lamp:
                if elements[0].state[0] == 1 or elements[0].state[1] == 1 or elements[0].state[2] == 1 or elements[0].state[3] == 1:
                    return True
            else:
                if elements[1].state[0] == 1 or elements[1].state[1] == 1 or elements[1].state[2] == 1 or elements[1].state[3] == 1:
                    return True
    elif level == 5:
        return True
    elif level == 6:
        return True
    elif level == 7:
        return True
    elif level == 8:
        return True
    elif level == 9:
        return True
    elif level == 10:
        return True
    elif level == 11:
        return True
    elif level == 12:
        return True
    elif level == 13:
        return True
    elif level == 14:
        return True
    elif level == 15:
        return True
    elif level == 16:
        return True
    elif level == 17:
        return True
    elif level == 18:
        return True
    return False

def setup(level, elements, wires, screen):
    if level == 1:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 14, 4, False))
        wires.append(Wire.Wire(14 * 40 - 5 + 25, 10 * 40 - 5, elements[0], 0, 14 * 40 - 5 + 25, 4 * 40 - 5 + 50, elements[1], 2))
        elements[0].wires_connected.append(wires[-1])
        elements[1].wires_connected.append(wires[-1])
    elif level == 2:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 14, 4, False))
    elif level == 3:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 14, 4, False))
        elements.append(Lamp.Lamp(screen, 11, 4, False))
        elements.append(Lamp.Lamp(screen, 17, 4, False))
    elif level == 5 or level == 7 or level == 8 or level == 9 or level == 11:
        elements.append(Source.Source(screen, 12, 10, False))
        elements.append(Source.Source(screen, 16, 10, False))
        elements[0].state = [0, 0, 0, 0]
        elements[1].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 14, 4, False))
    elif level == 6:
        elements.append(Source.Source(screen, 17, 10, False))
        elements.append(Source.Source(screen, 13, 8, False))
        elements[0].state = [0, 0, 0, 0]
        elements[1].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 13, 2, False))
    elif level == 10:
        elements.append(Source.Source(screen, 8, 10, False))
        elements.append(Source.Source(screen, 11, 10, False))
        elements.append(Source.Source(screen, 14, 10, False))
        elements.append(Source.Source(screen, 17, 10, False))
        elements.append(Source.Source(screen, 20, 10, False))
        elements[0].state = [1, 1, 1, 1]
        elements[1].state = [0, 0, 0, 0]
        elements[2].state = [1, 1, 1, 1]
        elements[3].state = [1, 1, 1, 1]
        elements[4].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 8, 4, False))
    elif level == 12:
        elements.append(Source.Source(screen, 28, 7, False))
        elements[0].state = [0, 0, 0, 0]
        elements.append(Source.Source(screen, 2, 11, False))
        elements.append(Source.Source(screen, 5, 11, False))
        elements.append(Source.Source(screen, 8, 11, False))
        elements.append(Source.Source(screen, 11, 11, False))
        elements.append(Source.Source(screen, 16, 11, False))
        elements.append(Source.Source(screen, 19, 11, False))
        elements.append(Source.Source(screen, 22, 11, False))
        elements.append(Source.Source(screen, 25, 11, False))
        elements.append(Lamp.Lamp(screen, 9, 4, False))
        elements.append(Lamp.Lamp(screen, 12, 4, False))
        elements.append(Lamp.Lamp(screen, 15, 4, False))
        elements.append(Lamp.Lamp(screen, 18, 4, False))
    elif level == 13:
        elements.append(Source.Source(screen, 12, 13, False))
        elements.append(Source.Source(screen, 16, 13, False))
        elements.append(Source.Source(screen, 19, 10, False))
        elements[0].state = [0, 0, 0, 0]
        elements[1].state = [0, 0, 0, 0]
        elements[2].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 14, 2, False))
    elif level == 14:
        elements.append(Source.Source(screen, 2, 11, False))
        elements.append(Source.Source(screen, 5, 11, False))
        elements.append(Source.Source(screen, 8, 11, False))
        elements.append(Source.Source(screen, 11, 11, False))
        elements.append(Source.Source(screen, 17, 11, False))
        elements.append(Source.Source(screen, 20, 11, False))
        elements.append(Source.Source(screen, 23, 11, False))
        elements.append(Source.Source(screen, 26, 11, False))
        elements[0].state = [0, 0, 0, 0]
        elements[1].state = [0, 0, 0, 0]
        elements[2].state = [0, 0, 0, 0]
        elements[3].state = [0, 0, 0, 0]
        elements[4].state = [0, 0, 0, 0]
        elements[5].state = [0, 0, 0, 0]
        elements[6].state = [0, 0, 0, 0]
        elements[7].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 8, 3, False))
        elements.append(Lamp.Lamp(screen, 11, 3, False))
        elements.append(Lamp.Lamp(screen, 14, 3, False))
        elements.append(Lamp.Lamp(screen, 17, 3, False))
        elements.append(Lamp.Lamp(screen, 20, 3, False))
    elif level == 15:
        elements.append(Source.Source(screen, 4, 12, False))
        elements.append(Source.Source(screen, 7, 12, False))
        elements.append(Source.Source(screen, 10, 12, False))
        elements.append(Source.Source(screen, 15, 12, False))
        elements.append(Source.Source(screen, 18, 12, False))
        elements.append(Source.Source(screen, 21, 12, False))
        elements[0].state = [0, 0, 0, 0]
        elements[1].state = [0, 0, 0, 0]
        elements[2].state = [0, 0, 0, 0]
        elements[3].state = [0, 0, 0, 0]
        elements[4].state = [0, 0, 0, 0]
        elements[5].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 5, 2, False))
        elements.append(Lamp.Lamp(screen, 8, 2, False))
        elements.append(Lamp.Lamp(screen, 11, 2, False))
        elements.append(Lamp.Lamp(screen, 14, 2, False))
        elements.append(Lamp.Lamp(screen, 17, 2, False))
        elements.append(Lamp.Lamp(screen, 20, 2, False))
    elif level == 16:
        elements.append(Source.Source(screen, 14, 13, False))
        elements[0].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 14, 1, False))
    elif level == 17:
        elements.append(Source.Source(screen, 14, 12, False))
        elements[0].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 3, 2, False))
        elements.append(Lamp.Lamp(screen, 6, 2, False))
        elements.append(Lamp.Lamp(screen, 9, 2, False))
        elements.append(Lamp.Lamp(screen, 12, 2, False))
        elements.append(Lamp.Lamp(screen, 16, 2, False))
        elements.append(Lamp.Lamp(screen, 19, 2, False))
        elements.append(Lamp.Lamp(screen, 22, 2, False))
        elements.append(Lamp.Lamp(screen, 25, 2, False))
    elif level == 18:
        elements.append(Source.Source(screen, 1, 13, False))
        elements.append(Source.Source(screen, 4, 13, False))
        elements.append(Source.Source(screen, 7, 13, False))
        elements.append(Source.Source(screen, 10, 13, False))
        elements.append(Source.Source(screen, 15, 13, False))
        elements.append(Source.Source(screen, 18, 13, False))
        elements.append(Source.Source(screen, 21, 13, False))
        elements.append(Source.Source(screen, 24, 13, False))
        elements[0].state = [0, 0, 0, 0]
        elements[1].state = [0, 0, 0, 0]
        elements[2].state = [0, 0, 0, 0]
        elements[3].state = [0, 0, 0, 0]
        elements[4].state = [0, 0, 0, 0]
        elements[5].state = [0, 0, 0, 0]
        elements[6].state = [0, 0, 0, 0]
        elements[7].state = [0, 0, 0, 0]
        elements.append(Lamp.Lamp(screen, 1, 1, False))
        elements.append(Lamp.Lamp(screen, 4, 1, False))
        elements.append(Lamp.Lamp(screen, 7, 1, False))
        elements.append(Lamp.Lamp(screen, 10, 1, False))
        elements.append(Lamp.Lamp(screen, 15, 1, False))
        elements.append(Lamp.Lamp(screen, 18, 1, False))
        elements.append(Lamp.Lamp(screen, 21, 1, False))
        elements.append(Lamp.Lamp(screen, 24, 1, False))