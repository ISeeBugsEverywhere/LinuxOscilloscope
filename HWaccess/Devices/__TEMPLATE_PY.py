import os
import sys
import numpy as np
import math
from HWaccess.USBTMC import USBTMC # -- for USBTMC
import vxi11 # -- for LXI instruments

class Oscilloscope:
    """
    TEMPLATE
    """
    def __init__(self):
        # ====================
        # THESE ATTRIBUTES MUST BE IMPLEMENTED:
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
        # === END OF NECESSARY ATTRIBUTES ==========
        # BELOW any attribute can be implemented
        pass
    # ============================================================
    # FROM HERE:
    # ALL THESE METHODS MUST BE IMPLEMENTED:
    # ============================================================
    def init_device(port, params):
        pass

    def get_name():
        pass

    def reset():
        pass

    def unlock_key():
        pass

    def save_all(fname, path):
        pass

    def screenshot(fname, path):
        pass

    def ask(cmd:str):
        pass

    def write(cmd:str):
        pass

    def get_xy(channel:str):
        pass



    # =============================================================
    # END OF REQUIRED METHODS
    # =============================================================

    # =============================================================
    # STARTING FROM HERE
    # any necessary method can be described here
    # =============================================================