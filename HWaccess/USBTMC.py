import os
import time
import numpy as np
class USBTMC:
    """
    Very Simple usbmtc device
    """

    def __init__(self, device):
        self.device = device
        self.FILE = os.open(self.device, os.O_RDWR)

    def write(self, command):
        try:
            os.write(self.FILE, str.encode(command))
            return None, 0
        except Exception as ex:
            return str(ex), -1
            pass

    def read(self, length=4000):
        '''

        :param length: length of data to read
        :return:
        '''
        return os.read(self.FILE, length)

    def close(self):
        os.close(self.FILE)

    def ask(self, cmd, sleep=0, length=4000):
        """
        Imitates vxi11 ask command, therefore returns a string
        :param cmd:
        :return:
        """
        self.write(cmd)
        time.sleep(sleep)
        a = self.read_ask(length)
        return str(a.decode('utf-8'))

    def read_ask(self, length=4000):
        return os.read(self.FILE, length).splitlines()[0]

