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
        if length != 0:
            return os.read(self.FILE, length)
        else:
            return os.read(self.FILE)

    def close(self):
        os.close(self.FILE)

    def ask(self, cmd, sleep=1, length=4000):
        """
        Imitates vxi11 ask command, therefore returns a string
        :param cmd:
        :return:
        """
        self.write(cmd)
        time.sleep(sleep)
        a = self.read_ask(length)
        a_ = ''
        try:
            a_ = str(a.decode('utf-8'))
        except:
            print(a)
            a_ = str(np.frombuffer(a))
        return a_

    def read_ask(self, length=4000):
        try:
            return os.read(self.FILE, length).splitlines()[0]
        except:
            return os.read(self.FILE, length)

    def ask_(self, cmd, delay=1, length=4000):
        string = None
        try:
            self.write(cmd)
            time.sleep(delay)
            ret = self.read(length)
            string = str(ret, encoding='utf-8', errors='ignore')
        except Exception as ex:
            string = 'USBTMC failed!::EX::'+str(ex)
            print('USBTMC failed:')
            print(str(ex))
        return string
