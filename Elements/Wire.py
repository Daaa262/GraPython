class Wire:
    def __init__(self, pos_x1, pos_y1, element1, joint1, pos_x2, pos_y2, element2, joint2):
        self.pos_x1 = pos_x1
        self.pos_y1 = pos_y1
        self.element1 = element1
        self.joint1 = joint1
        self.pos_x2 = pos_x2
        self.pos_y2 = pos_y2
        self.element2 = element2
        self.joint2 = joint2
        self.powered = False