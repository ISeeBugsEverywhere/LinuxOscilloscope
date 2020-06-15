import os
import sys
import numpy as np
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
        self.CH_ARR = [self.CH1, self.CH2]
        self.CH_SIZE = 2
        pass

    def init_device(self, port:str, params):
        self.device = None
        pass

    def get_name(self):
        return "DEMO device"

    def get_data_points_from_channel(self, CH):
        time = np.arange(0, 1000)
        y = np.random.randn(1,1000)[0]
        return y, time, "S"

    def get_xy(self, CH:str):
        """

        :param CH: channel
        :return: data, time, time_unit, data will be in volts, time in time units, everything will be in lists
        """
        data, time, t_unit = self.get_data_points_from_channel(CH)
        return data.tolist(), time.tolist(), t_unit