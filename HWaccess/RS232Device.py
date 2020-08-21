import os
import time
import serial
import numpy as np
import traceback


class RS232Device():
    def __init__(self, port):
        self.serial = serial.Serial()
        self.serial.setPort(port)
        self._endline = '\r\n'
        pass

    def _setup_port(self, params:dict, endline='\r\n'):
        self.serial.applySettingsDict(params)
        self.serial.timeout = 2
        self._endline = endline
        self.serial.open()
        if self.serial.isOpen():
            print('OPENED')
            self.serial.write(str.encode("*RST"))
        pass

    def read(self, size:1000):
        try:
            rbytes = self.serial.read(size)
            return rbytes,  0
        except Exception as ex:
            return str(ex), -1


    def write(self, cmd:str):
        try:
            if self.serial.isOpen():
                bint = self.serial.write(cmd.encode('utf-8'))
                print('bint ', bint)
                if bint > 0:
                    return str(bint), 0
                else:
                    return "Bytes wasn't written", -1
            elif not self.serial.isOpen():
                self.serial.open()
                bint = self.serial.write(cmd.encode('utf-8'))
                print('open fork, bint ', bint)
                if bint > 0:
                    return str(bint), 0
                else:
                    return "Bytes wasn't written", -1
        except Exception as ex:
            return str(ex), -1

    def ask(self, cmd, sleep=1, length=4000):
        """
        Returns a string, imitates a LXI command
        :param cmd:
        :param sleep:
        :param length:
        :return:
        """
        string = ''
        try:
            if self.serial.isOpen():
                self.serial.write(cmd)
                time.sleep(sleep)
                a = self.serial.read_until(self._endline, length)
                return a.decode('utf-8')
        except Exception as ex:
            traceback.print_exc()
            string = str(ex)
            return string

    def close(self):
        self.serial.close()

