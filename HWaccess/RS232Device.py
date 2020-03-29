import os
import time
import serial


class RS232Device():
    def __init__(self, port):
        self.serial = serial.Serial()
        self.serial.setPort(port)
        pass

    def ask(self, cmd:str):
        pass

    def write(self, cmd:str):
        pass