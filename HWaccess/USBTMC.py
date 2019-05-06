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
        self._encoding = None
        self._errors = None

    def set_encoding(self, encoding:str = 'utf-8'):
        '''
        Sets encoding used in decoding of bytes

        :param encoding: 'utf-8', 'ascii', others can be too.
        :return:
        '''
        self._encoding = encoding
        pass

    def set_errors_behavior(self, errors:str='ignore'):
        '''
        If decoding of bytes fails, this parameter will be used how to treat those errors

        :param errors:
        :return:
        '''
        self._errors = errors
        pass

    def write(self, command):
        os.write(self.FILE, str.encode(command))

    def read(self, length=4000):
        '''

        :param length: length of data to read
        :return:
        '''
        return os.read(self.FILE, length)

    def getName(self):
        self.write("*IDN?")
        return self.read(300)

    def sendReset(self):
        self.write("*RST")

    def closeDevice(self):
        os.close(self.FILE)

    def ask_string(self, cmd, delay=1, length=9000):
        string = None
        print(cmd, ' will be executed on ask_string statement')
        try:
            self.write(cmd)
            time.sleep(delay)
            print('Answer')
            ret = self.read(length)
            string = str(ret, encoding=self._encoding, errors=self._errors)
        except Exception as ex:
            string = 'USBTMC failed!'
            print('USBTMC failed:')
            print(str(ex))
        return string

    def ask(self, cmd, delay=1, length=4000):
        ret = None
        print(cmd, 'will be executed on ask statement')
        try:
            self.write(cmd)
            time.sleep(delay)
            ret = self.read(length)
            #string = str(ret, encoding=self._encoding, errors=self._errors)
        except Exception as ex:
            ret = 'USBTMC failed!'
            print('USBTMC failed:')
            print(str(ex))
        return ret

    def ask_values(self, cmd, delay=1, length=9000):
        array = None
        print(cmd, ' will be executed on ask_values statement')
        try:
            self.write(cmd)
            time.sleep(delay)
            ret = self.read(length)
            array = np.frombuffer(ret, 'B')
        except Exception as ex:
            array = 'USBTMC failed!'
            print('USBTMC failed:')
            print(str(ex))
        return array
        pass
