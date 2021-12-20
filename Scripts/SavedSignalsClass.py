#!/usr/bin/python3

class SavedSignal():
    def __init__(self, x, y, name, color, EQ = 'y'):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.width = 2.0
        self.eq = EQ


class Signal():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
