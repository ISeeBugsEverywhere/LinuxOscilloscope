import os
import sys
import numpy as np
import math
from HWaccess.USBTMC import USBTMC # -- for USBTMC
# import vxi11 # -- for LXI instruments

class Oscilloscope:
    """
    Rigol DHO 802 wrapper
    """
    def __init__(self):
        # ====================
        # THESE ATTRIBUTES MUST BE IMPLEMENTED:
        self.device = None
        self.t_name="Rigol DHO802 (USB)"
        self.idn = None
        self.mode = "NORM"
        self.CH1 = "CHAN1"
        self.CH2 = "CHAN2"
        self.CH3 = "CHAN3"
        self.CH4 = "CHAN4"
        self.CH_ARR = [self.CH1, self.CH2, self.CH3, self.CH4]
        self.CH_SIZE = 4
        # === END OF NECESSARY ATTRIBUTES ==========
        # BELOW any attribute can be implemented
        pass
    # ============================================================
    # FROM HERE:
    # ALL THESE METHODS MUST BE IMPLEMENTED:
    # ============================================================
    def init_device(self, port, params):
        self.device = USBTMC(port)
        pass

    def get_name(self):
        r = self.device.ask('*IDN?')
        return r
        pass

    def reset(self):
        a, _ = self.device.write("*rst")
        if _ == -1:
            print(a)
        pass

    def unlock_key(self):
        pass

    def save_all(self,fname, path):
        pass

    def screenshot(self,fname, path):
        pass

    def ask(self, cmd:str, length=4000):
        resp = self.device.ask(cmd, length=length)
        return resp

    def write(self, cmd:str):
        r, _ = self.device.write(cmd)

    def get_xy(self, channel:str):
        pass



    # =============================================================
    # END OF REQUIRED METHODS
    # =============================================================

    # =============================================================
    # STARTING FROM HERE
    # any necessary method can be described here
    # =============================================================
    def read(self, length=4000):
        out = self.device.read(length=length)
        return out