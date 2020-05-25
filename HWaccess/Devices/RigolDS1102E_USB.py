import os
import sys
import numpy as np
from HWaccess.USBTMC import USBTMC



class Oscilloscope:
    """
    USBTMC based device!
    """
    def __init__(self):
        self.device = None
        self.t_name="RIGOL TEST NAME for class loading"
        pass

    def init_device(self, port:str):
        self.device = USBTMC(port)
        pass

    def get_name(self):
        a, _ = self.device.write("*idn?")
        if _ != -1:
            a_ = self.device.read(300)
            return  str(a_.decode())
        else:
            return a
        pass

    def reset(self):
        a, _ = self.device.write("*rst")
        if _ == -1:
            print(a)
        pass

    def close(self):
        self.device.close()

    #oscilloscope specific entries:

    def get_time_offset(self):
        '''
        # Get the timescale offset
        :return:
        '''
        self.device.write(":TIM:OFFS?")
        timeoffset = float(self.device.read(20))
        return timeoffset

    def get_time_scale(self):
        '''
        Get time scale
        # TIME SECTION ===========================
        # Get the timescale

        :return:
        '''
        self.device.write(":TIM:SCAL?")
        timescale = float(self.device.read(20))
        return timescale