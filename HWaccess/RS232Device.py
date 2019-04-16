import os
import time
from PyQt5.QtCore import pyqtSignal, QObject, QIODevice
from PyQt5 import QtSerialPort


class RS232Device(QObject, QtSerialPort):
    def __init__(self, port:QtSerialPort):
        super(RS232Device, self).__init__()
        self._port = port
        self._port.open(QIODevice.ReadWrite)
        self._output = None
        self._terminator= None
        self._encoding = None
        self._error_behavior = None
        pass

    def write(self, cmd:str):
        pass

    def read(self):
        bytes_waiting = self._port.BytesAvailable()
        pass

    def ask(self, cmd:str):
        pass