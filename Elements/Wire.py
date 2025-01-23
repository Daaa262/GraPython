import pygame

class Wire:
    def __init__(self, pos_x1, pos_y1, pos_x2, pos_y2, element1, element2, joint1, joint2):
        self.pos_x1 = pos_x1
        self.pos_x2 = pos_x2
        self.pos_y1 = pos_y1
        self.pos_y2 = pos_y2
        self.element1 = element1
        self.joint1 = joint1
        self.element2 = element2
        self.joint2 = joint2
        self.powered = False

    def update(self):
        if self.element1.state[self.joint1] == 1 or self.element2.state[self.joint2] == 1:
            self.powered = True
        else:
            self.powered = False