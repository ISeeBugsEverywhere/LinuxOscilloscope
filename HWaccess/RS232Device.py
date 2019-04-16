import os
import time
from PyQt5.QtCore import pyqtSignal, QObject, QIODevice
from PyQt5 import QtSerialPort


class RS232Device(QObject, QtSerialPort):
    def __init__(self, port:QtSerialPort.QSerialPort()):
        super(RS232Device, self).__init__()
        self._port = QtSerialPort.QSerialPort()
        # self._port = port
        self._port.open(QIODevice.ReadWrite)
        self._output = None
        self._terminator= None
        self._encoding = None
        self._error_behavior = None
        self._line_end = None
        pass

    def write(self, cmd:str):
        self._port.write(bytes((cmd)+self._line_end, self._encoding))
        pass

    def read(self):
        bytes_waiting = self._port.BytesAvailable()
        pass

    def ask(self, cmd:str):
        pass