import os
import sys
import numpy as np
import math
from HWaccess.USBTMC import USBTMC



class Oscilloscope:
    """
    Demo device
    """
    def __init__(self):
        self.device = None
        self.t_name="Demo device"
        self.idn = None
        self.mode = "NORM"
        self.CH1 = "CHAN1"
        self.CH2 = "CHAN2"
        self.CH3 = "CHAN3"
        self.CH4 = "CHAN4"
        self.CH_ARR = [self.CH1, self.CH2, self.CH3, self.CH4]
        self.CH_SIZE = 4
        pass

    def init_device(self, port:str, params):
        self.device = None
        pass

    def get_name(self):
        return "DEMO IDN :: 42 (the Answer)"

    def close(self):
        pass

    def get_data_points_from_channel(self, CH):
        time = np.arange(0, 1000)
        var = np.random.randint(50)/10.0
        y = []
        if CH == self.CH1:
            a = np.random.randn(1,1000)[0]
            y = a.tolist()
        elif CH == self.CH2:
            # y_ = np.random.randn(1,1000)[0]
            y = [var*math.cos(i*math.pi/180.0) for i in time]
        elif CH == self.CH3:
            # y_ = np.random.randn(1,1000)[0]
            y = [var*math.sin(i*math.pi/180.0) for i in time]
        elif CH == self.CH4:
            # y_ = np.random.randn(1,1000)[0]
            y = [var*math.cos(2*i*math.pi/180.0) for i in time]
        return y, time.tolist(), "S"

    def get_xy(self, CH:str):
        """

        :param CH: channel
        :return: data, time, time_unit, data will be in volts, time in time units, everything will be in lists
        """
        data, time, t_unit = self.get_data_points_from_channel(CH)
        return data, time, t_unit

    def ask(self, cmd:str):
        return "demo ask: "+cmd

    def write(self, cmd:str):
        pass