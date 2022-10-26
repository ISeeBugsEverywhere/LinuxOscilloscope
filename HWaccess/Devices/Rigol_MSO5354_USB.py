import os
import sys
import time

import numpy as np
import platform
# if "windows" in platform.system().lower():
#     from HWaccess.USBTMC_mod import USBTMC
# elif "linux" in platform.system().lower():
from HWaccess.USBTMC import USBTMC


class Oscilloscope:
    """
    Rigol, an USBTMC based device!
    """

    def __init__(self):
        self.device = None
        self.t_name = "Rigol MSO5354 (USB) NOT IMPLEMENTED YET"
        self.idn = None
        self.mode = "NORM"
        self.CH1 = "CHAN1"
        self.CH2 = "CHAN2"
        self.CH3 = "CHAN3"
        self.CH4 = "CHAN4"
        self.CH_ARR = [self.CH1, self.CH2, self.CH3, self.CH4]
        self.CH_SIZE = 4
        pass

    def init_device(self, port: str, params):
        self.device = USBTMC(port)
        pass

    def get_name(self):
        a, _ = self.device.write("*idn?")
        if _ != -1:
            a_ = self.device.read(300)
            return str(a_.decode())
        else:
            return a
        pass

    def reset(self):
        a, _ = self.device.write("*rst")
        if _ == -1:
            print(a)
        pass

    def close(self):
        # self.unlock_key()
        self.device.close()

    def stop(self):
        self.device.write(":STOP")

    # oscilloscope specific entries:
    def get_xy(self, CH: str):
        """

        :param CH: channel
        :return: data, time, time_unit, data will be in volts, time in time units, everything will be in lists
        """
        t_unit = None
        data = None
        return data.tolist(), time.tolist(), t_unit

    def ask(self, cmd: str, length=4000):
        return self.device.ask(cmd, length=length)

    def write(self, cmd: str):
        self.device.write(cmd)
        pass

    def screenshot(self, fname="None", path="E:"):
        """
        writes a screenshot (*.BMP) into U:\ disk
        :return:
        """
        pass
