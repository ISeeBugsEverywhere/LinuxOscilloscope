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

    def _bytes_to_array(self, bts):
        """
        Specific functionality to obtain useful information from the rs232 device
        :param bts:
        :return:
        """
        pass

    def ask(self, cmd:str):
        try:
            if self.serial.is_open():
                bint = self.serial.write(cmd.encode('utf-8'))
                time.sleep(1.0)
                if bint > 0:
                    answ = self.serial.read_until(terminator=self._endline)
                    return answ, 0
                else:
                    return "Bytes written - 0", -1
        except Exception as ex:
            return str(ex), -1
        pass

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


    def getName(self):
        name = self.ask("*idn?")
        return name