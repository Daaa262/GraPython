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
        text_surface = font.render("krok,gdy dostanie sygnal.", True, (0, 0, 0))
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
    elif level == 5:
        return [0] * 14
    elif level == 6:
        return [0, 1, 0, 1] + [0] * 10
    elif level == 7:
        return [0, 0, 0, 1, 1] + [0] * 9
    elif level == 8:
        return [0, 0, 1, 1] + [0] * 10
    elif level == 9:
        return [0, 0, 1, 1] + [0] * 10
    elif level == 10:
        return [0, 0, 0, 1, 2] + [0] * 9
    elif level == 11:
        return [0, 0, 0, 2] + [0] * 10
    elif level == 12:
        return [0, 0, 0, 0, 1, 8] + [0] * 8
    elif level == 13:
        return [0, 0, 0, 0, 0, 3, 0, 0, 2] + [0] * 5
    elif level == 14:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4] + [0] * 3
    elif level == 15:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2] + [0] * 2
    elif level == 16:
        return [0, 0, 3, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif level == 17:
        return [0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 8, 0]
    else:
        return [-1] * 14

def step(elements, wires):
    for element in elements:
        element.read_input()
    for wire in wires:
        wire.powered = False
    for element in elements:
        element.set_output()

def stabilize(elements, wires):
    current_state = [wire.powered for wire in wires]
    states = []
    while current_state not in states:
        states.append(current_state)
        step(elements, wires)
        current_state = [wire.powered for wire in wires]

def element_on(element):
    if element.state[0] == 1 or element.state[1] == 1 or element.state[2] == 1 or element.state[3] == 1:
        return True
    else:
        return False

def lamp_state_changed_during_stabilization(elements, wires, lamp):
    lamp_state = element_on(lamp)
    current_state = [wire.powered for wire in wires]
    states = []
    while current_state not in states:
        states.append(current_state)
        step(elements, wires)
        if element_on(lamp) != lamp_state:
            return True
        current_state = [wire.powered for wire in wires]
    return False

def check_conditions(level, elements, wires):
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
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        stabilize(elements, wires)
        if element_on(elements[2]):
            return False
        elements[0].state = [1] * 4
        elements[1].state = [0] * 4
        stabilize(elements, wires)
        if not element_on(elements[2]):
            return False
        elements[0].state = [0] * 4
        elements[1].state = [1] * 4
        stabilize(elements, wires)
        if not element_on(elements[2]):
            return False
        elements[0].state = [1] * 4
        elements[1].state = [1] * 4
        stabilize(elements, wires)
        if not element_on(elements[2]):
            return False
        return True
    elif level == 6:
        elements[0].state = [0] * 4
        stabilize(elements, wires)
        if not element_on(elements[1]):
            return False
        elements[0].state = [1] * 4
        stabilize(elements, wires)
        if element_on(elements[1]):
            return False
        return True
    elif level == 7:
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        stabilize(elements, wires)
        if element_on(elements[2]):
            return False
        elements[0].state = [1] * 4
        elements[1].state = [0] * 4
        stabilize(elements, wires)
        if element_on(elements[2]):
            return False
        elements[0].state = [0] * 4
        elements[1].state = [1] * 4
        stabilize(elements, wires)
        if element_on(elements[2]):
            return False
        elements[0].state = [1] * 4
        elements[1].state = [1] * 4
        stabilize(elements, wires)
        if not element_on(elements[2]):
            return False
        return True
    elif level == 8:
        elements[0].state = [0] * 4
        stabilize(elements, wires)
        if element_on(elements[1]):
            return False
        if lamp_state_changed_during_stabilization(elements, wires, elements[1]):
            return False
        return True
    elif level == 9:
        elements[0].state = [0] * 4
        stabilize(elements, wires)
        if element_on(elements[1]):
            return False
        elements[0].state = [1] * 4
        if not lamp_state_changed_during_stabilization(elements, wires, elements[1]):
            return False
        stabilize(elements, wires)
        state = [wire.powered for wire in wires]
        step(elements, wires)
        if not element_on(elements[1]):
            return False
        step(elements, wires)
        if element_on(elements[1]):
            return False
        step(elements, wires)
        if element_on(elements[1]):
            return False
        step(elements, wires)
        if not element_on(elements[1]):
            return False
        if [wire.powered for wire in wires] != state:
            return False
        return True
    elif level == 10:
        for i in range(2 ** 5):
            for j in range(5):
                elements[j].state = [(i >> j) & 1] * 4
            stabilize(elements, wires)
            if i == 0b10110:
                if not element_on(elements[5]):
                    return False
            else:
                if element_on(elements[5]):
                    return False
        return True
    elif level == 11:
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        stabilize(elements, wires)
        if element_on(elements[2]):
            return False
        elements[0].state = [1] * 4
        elements[1].state = [0] * 4
        stabilize(elements, wires)
        if not element_on(elements[2]):
            return False
        elements[0].state = [0] * 4
        elements[1].state = [1] * 4
        stabilize(elements, wires)
        if not element_on(elements[2]):
            return False
        elements[0].state = [1] * 4
        elements[1].state = [1] * 4
        stabilize(elements, wires)
        if element_on(elements[2]):
            return False
        return True
    elif level == 12:
        for i in range(2 ** 8):
            for j in range(8):
                elements[j + 1].state = [(i >> j) & 1] * 4
            elements[0].state = [0] * 4
            stabilize(elements, wires)
            if element_on(elements[9]) != element_on(elements[5]) or element_on(elements[10]) != element_on(elements[6]) or element_on(elements[11]) != element_on(elements[7]) or element_on(elements[12]) != element_on(elements[8]):
                return False
            elements[0].state = [1] * 4
            stabilize(elements, wires)
            if element_on(elements[9]) != element_on(elements[1]) or element_on(elements[10]) != element_on(elements[2]) or element_on(elements[11]) != element_on(elements[3]) or element_on(elements[12]) != element_on(elements[4]):
                return False
        return True
    elif level == 13:
        for i in range(2 ** 3):
            source = 0
            for j in range(3):
                if (i >> j) & 1 == 1:
                    elements[j].state = [1] * 4
                    source += 1
                else:
                    elements[j].state = [0] * 4
            stabilize(elements, wires)

            lamp = 0
            for j in range(2):
                if element_on(elements[3 + j]):
                    lamp += 2 ** j

            if source != lamp:
                return False
        return True
    elif level == 14:
        for i in range(2 ** 8):
            source = 0
            for j in range(8):
                if (i >> j) & 1 == 1:
                    elements[j].state = [1] * 4
                    source += 2 ** (j % 4)
                else:
                    elements[j].state = [0] * 4
            stabilize(elements, wires)

            lamp = 0
            for j in range(5):
                if element_on(elements[8 + j]):
                    lamp += 2 ** j

            if source != lamp:
                return False
        return True
    elif level == 15:
        for i in range(2 ** 6):
            source1 = 0
            source2 = 0
            for j in range(6):
                if (i >> j) & 1 == 1:
                    elements[j].state = [1] * 4
                    if j < 3:
                        source1 += 2 ** j
                    else:
                        source2 += 2 ** (j - 3)
                else:
                    elements[j].state = [0] * 4
            stabilize(elements, wires)

            lamp = 0
            for j in range(6):
                if element_on(elements[6 + j]):
                    lamp += 2 ** j

            if source1 * source2 != lamp:
                return False
        return True
    elif level == 16:
        elements[0].state = [0] * 4
        stabilize(elements, wires)

        initial_state = [wire.powered for wire in wires]
        while True:
            lamp_state = element_on(elements[1])
            elements[0].state = [1] * 4
            if lamp_state_changed_during_stabilization(elements, wires, elements[1]) and lamp_state_changed_during_stabilization(elements, wires, elements[1]):
                return False
            if element_on(elements[1]) == lamp_state:
                return False

            elements[0].state = [0] * 4
            if lamp_state_changed_during_stabilization(elements, wires, elements[1]):
                return False

            lamp_state = element_on(elements[1])
            elements[0].state = [1] * 4
            if lamp_state_changed_during_stabilization(elements, wires, elements[1]) and lamp_state_changed_during_stabilization(elements, wires, elements[1]):
                return False
            if element_on(elements[1]) == lamp_state:
                return False

            elements[0].state = [0] * 4
            if lamp_state_changed_during_stabilization(elements, wires, elements[1]):
                return False

            if [wire.powered for wire in wires] == initial_state:
                break
        return True
    elif level == 17:
        elements[0].state = [0] * 4
        stabilize(elements, wires)

        state = 0
        for i in range(8):
            if element_on(elements[i + 1]):
                state += 2 ** i
        previous = state
        loop = state

        states = []
        initial_state = [wire.powered for wire in wires]
        while initial_state not in states:
            elements[0].state = [1] * 4
            stabilize(elements, wires)

            state = 0
            for i in range(8):
                if element_on(elements[i + 1]):
                    state += 2 ** i
            if state != (previous + 1) % (2 ** 8):
                return False
            previous = (previous + 1) % (2 ** 8)

            elements[0].state = [0] * 4
            stabilize(elements, wires)

            state = 0
            for i in range(8):
                if element_on(elements[i + 1]):
                    state += 2 ** i
            if state != previous:
                return False

            if state == loop:
                states.append([wire.powered for wire in wires])

        return True
    elif level == 18:
        for i in range(2 ** 8):
            source1 = 0
            source2 = 0
            for j in range(8):
                if (i >> j) & 1 == 1:
                    elements[j].state = [1] * 4
                    if j < 4:
                        source1 += 2 ** j
                    else:
                        source2 += 2 ** (j - 4)
                else:
                    elements[j].state = [0] * 4
            stabilize(elements, wires)

            lamp1 = 0
            lamp2 = 0
            for j in range(4):
                if element_on(elements[8 + j]):
                    lamp1 += 2 ** j
                if element_on(elements[12 + j]):
                    lamp2 += 2 ** j

            if source1 == 0 and (lamp1 != 0 or lamp2 != 0):
                return False

            if source2 // source1 != lamp2 or source2 % source1 != lamp1:
                return False
        return True
    return False

def setup(level, elements, wires, screen):
    if level == 1:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 14, 4, False))
        wires.append(Wire.Wire(14 * 40 - 5 + 25, 10 * 40 - 5, elements[0], 0, 14 * 40 - 5 + 25, 4 * 40 - 5 + 50, elements[1], 2))
        elements[0].wires_connected.append(wires[-1])
        elements[1].wires_connected.append(wires[-1])
    elif level == 2:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 14, 4, False))
    elif level == 3:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 14, 4, False))
        elements.append(Lamp.Lamp(screen, 11, 4, False))
        elements.append(Lamp.Lamp(screen, 17, 4, False))
    elif level == 5 or level == 7 or level == 11:
        elements.append(Source.Source(screen, 12, 10, False))
        elements.append(Source.Source(screen, 16, 10, False))
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 14, 4, False))
    elif level == 6 or level == 8 or level == 9:
        elements.append(Source.Source(screen, 14, 10, False))
        elements[0].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 14, 4, False))
    elif level == 10:
        elements.append(Source.Source(screen, 20, 10, False))
        elements.append(Source.Source(screen, 17, 10, False))
        elements.append(Source.Source(screen, 14, 10, False))
        elements.append(Source.Source(screen, 11, 10, False))
        elements.append(Source.Source(screen, 8, 10, False))
        elements[0].state = [0] * 4
        elements[1].state = [1] * 4
        elements[2].state = [1] * 4
        elements[3].state = [0] * 4
        elements[4].state = [1] * 4
        elements.append(Lamp.Lamp(screen, 8, 4, False))
    elif level == 12:
        elements.append(Source.Source(screen, 28, 7, False))
        elements[0].state = [0] * 4
        elements.append(Source.Source(screen, 25, 11, False))
        elements.append(Source.Source(screen, 22, 11, False))
        elements.append(Source.Source(screen, 19, 11, False))
        elements.append(Source.Source(screen, 16, 11, False))
        elements.append(Source.Source(screen, 11, 11, False))
        elements.append(Source.Source(screen, 8, 11, False))
        elements.append(Source.Source(screen, 5, 11, False))
        elements.append(Source.Source(screen, 2, 11, False))
        elements.append(Lamp.Lamp(screen, 18, 4, False))
        elements.append(Lamp.Lamp(screen, 15, 4, False))
        elements.append(Lamp.Lamp(screen, 12, 4, False))
        elements.append(Lamp.Lamp(screen, 9, 4, False))
    elif level == 13:
        elements.append(Source.Source(screen, 19, 10, False))
        elements.append(Source.Source(screen, 16, 13, False))
        elements.append(Source.Source(screen, 12, 13, False))
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        elements[2].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 16, 2, False))
        elements.append(Lamp.Lamp(screen, 12, 2, False))
    elif level == 14:
        elements.append(Source.Source(screen, 26, 11, False))
        elements.append(Source.Source(screen, 23, 11, False))
        elements.append(Source.Source(screen, 20, 11, False))
        elements.append(Source.Source(screen, 17, 11, False))
        elements.append(Source.Source(screen, 11, 11, False))
        elements.append(Source.Source(screen, 8, 11, False))
        elements.append(Source.Source(screen, 5, 11, False))
        elements.append(Source.Source(screen, 2, 11, False))
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        elements[2].state = [0] * 4
        elements[3].state = [0] * 4
        elements[4].state = [0] * 4
        elements[5].state = [0] * 4
        elements[6].state = [0] * 4
        elements[7].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 20, 3, False))
        elements.append(Lamp.Lamp(screen, 17, 3, False))
        elements.append(Lamp.Lamp(screen, 14, 3, False))
        elements.append(Lamp.Lamp(screen, 11, 3, False))
        elements.append(Lamp.Lamp(screen, 8, 3, False))
    elif level == 15:
        elements.append(Source.Source(screen, 21, 13, False))
        elements.append(Source.Source(screen, 18, 13, False))
        elements.append(Source.Source(screen, 15, 13, False))
        elements.append(Source.Source(screen, 10, 13, False))
        elements.append(Source.Source(screen, 7, 13, False))
        elements.append(Source.Source(screen, 4, 13, False))
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        elements[2].state = [0] * 4
        elements[3].state = [0] * 4
        elements[4].state = [0] * 4
        elements[5].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 20, 1, False))
        elements.append(Lamp.Lamp(screen, 17, 1, False))
        elements.append(Lamp.Lamp(screen, 14, 1, False))
        elements.append(Lamp.Lamp(screen, 11, 1, False))
        elements.append(Lamp.Lamp(screen, 8, 1, False))
        elements.append(Lamp.Lamp(screen, 5, 1, False))
    elif level == 16:
        elements.append(Source.Source(screen, 14, 13, False))
        elements[0].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 14, 1, False))
    elif level == 17:
        elements.append(Source.Source(screen, 14, 12, False))
        elements[0].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 25, 2, False))
        elements.append(Lamp.Lamp(screen, 22, 2, False))
        elements.append(Lamp.Lamp(screen, 19, 2, False))
        elements.append(Lamp.Lamp(screen, 16, 2, False))
        elements.append(Lamp.Lamp(screen, 12, 2, False))
        elements.append(Lamp.Lamp(screen, 9, 2, False))
        elements.append(Lamp.Lamp(screen, 6, 2, False))
        elements.append(Lamp.Lamp(screen, 3, 2, False))
    elif level == 18:
        elements.append(Source.Source(screen, 24, 13, False))
        elements.append(Source.Source(screen, 21, 13, False))
        elements.append(Source.Source(screen, 18, 13, False))
        elements.append(Source.Source(screen, 15, 13, False))
        elements.append(Source.Source(screen, 10, 13, False))
        elements.append(Source.Source(screen, 7, 13, False))
        elements.append(Source.Source(screen, 4, 13, False))
        elements.append(Source.Source(screen, 1, 13, False))
        elements[0].state = [0] * 4
        elements[1].state = [0] * 4
        elements[2].state = [0] * 4
        elements[3].state = [0] * 4
        elements[4].state = [0] * 4
        elements[5].state = [0] * 4
        elements[6].state = [0] * 4
        elements[7].state = [0] * 4
        elements.append(Lamp.Lamp(screen, 24, 1, False))
        elements.append(Lamp.Lamp(screen, 21, 1, False))
        elements.append(Lamp.Lamp(screen, 18, 1, False))
        elements.append(Lamp.Lamp(screen, 15, 1, False))
        elements.append(Lamp.Lamp(screen, 10, 1, False))
        elements.append(Lamp.Lamp(screen, 7, 1, False))
        elements.append(Lamp.Lamp(screen, 4, 1, False))
        elements.append(Lamp.Lamp(screen, 1, 1, False))