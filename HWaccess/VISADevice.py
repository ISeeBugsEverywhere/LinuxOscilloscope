import os
import time
import numpy as np

import pyvisa as visa

class VISADevice():
    def __init__(self, device:visa.Resource):
        # print(device, type(device))
        self.device = device
    
    def ask(self, cmd:str):
        r = self.device.query(cmd)
        return r
    
    def write(self, cmd:str):
        bts = self.device.write(cmd)
        return bts
    
    def close(self):
        self.device.close()
        pass

    def read(self, length=0):
        r = -1
        return -1