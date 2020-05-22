import os
import time
import serial
import numpy as np


class RS232Device():
    def __init__(self, port):
        self.serial = serial.Serial()
        self.serial.setPort(port)
        self._endline = '\n'
        pass

    def _setup_port(self, params:dict, endline='\n'):
        self.serial.applySettingsDict(params)
        self._endline = endline
        self.serial.open()
        pass

    def read(self, size:1000):
        try:
            rbytes = self.serial.read_until(self._endline, size)
            return rbytes,  0
        except Exception as ex:
            return str(ex), -1


    def write(self, cmd:str):
        try:
            if self.serial.is_open():
                bint = self.serial.write(cmd.encode('utf-8'))
                if bint > 0:
                    return str(bint), 0
                else:
                    return "Bytes wasn't written", -1
            pass
        except Exception as ex:
            return str(ex), -1

