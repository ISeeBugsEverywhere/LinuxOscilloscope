import os
import sys
import time
import numpy as np
import platform
# if "windows" in platform.system().lower():
#     from HWaccess.USBTMC_mod import USBTMC
# elif "linux" in platform.system().lower():
# from HWaccess.USBTMC import USBTMC
import pyvisa as visa

class Oscilloscope:
    """
    TEMPLATE
    """
    def __init__(self):
        # ====================
        # THESE ATTRIBUTES MUST BE IMPLEMENTED:
        self.device = None
        self.t_name="Rigol DS1202 (VISA USB)"
        self.idn = None
        self.mode = "NORM"
        self.CH1 = "CHAN1"
        self.CH2 = "CHAN2"
        # self.CH3 = "CHAN3"
        # self.CH4 = "CHAN4"
        self.CH_ARR = [self.CH1, self.CH2]
        self.CH_SIZE = 2
        # === END OF NECESSARY ATTRIBUTES ==========
        # BELOW any attribute can be implemented
        pass
    # ============================================================
    # FROM HERE:
    # ALL THESE METHODS MUST BE IMPLEMENTED:
    # ============================================================
    def init_device(self, port_device:visa.Resource, params):
        self.device = port_device
        pass

    def get_name(self):
        r = self.device.query('*IDN?')
        return r
        pass

    def reset(self):
        self.device.write("*RST")
        pass

    def unlock_key(self):
        pass

    def save_all(self, fname, path):
        pass

    def screenshot(self, fname, path):
        pass

    def ask(self, cmd:str):
        r = self.device.query(cmd)
        return r

    def write(self, cmd:str):
        r = self.device.write(cmd)
        return r
        pass

    def close(self):
        self.device.close()
        pass

    def get_xy(self, channel:str):
        rwd = self.get_waveform_data()
        volts = list(map(float, rwd[12:].split(',')))
        ps = self.get_waveform_preamble()
        # print(ps)
        times = [ps['xorigin'] + i*ps['xincrement'] for i in range(ps['points'])]
        return volts,times,'s'
        pass



    # =============================================================
    # END OF REQUIRED METHODS
    # =============================================================

    # =============================================================
    # STARTING FROM HERE
    # any necessary method can be described here
    # =============================================================

    def get_waveform_preamble(self):
        """
        Query and return all the waveform parameters.
        
        Returns:
            dict: A dictionary containing the waveform parameters with the following keys:
                - format: 0 (BYTE), 1 (WORD) or 2 (ASC)
                - type: 0 (NORMal), 1 (MAXimum) or 2 (RAW)
                - points: an integer between 1 and 24000000
                - count: the number of averages in the average sample mode and 1 in other modes
                - xincrement: the time difference between two neighboring points in the X direction
                - xorigin: the start time of the waveform data in the X direction
                - xreference: the reference time of the data point in the X direction
                - yincrement: the waveform increment in the Y direction
                - yorigin: the vertical offset relative to the "Vertical Reference Position" in the Y direction
                - yreference: the reference position in the Y direction
        """
        # Query the waveform preamble
        preamble_str = self.ask(":WAVeform:PREamble?")
        
        # Split the returned string into individual values
        preamble_values = preamble_str.split(',')
        
        # Create a dictionary with the parsed values
        preamble = {
            'format': int(preamble_values[0]),      # 0 (BYTE), 1 (WORD) or 2 (ASC)
            'type': int(preamble_values[1]),        # 0 (NORMal), 1 (MAXimum) or 2 (RAW)
            'points': int(preamble_values[2]),      # Number of points
            'count': int(preamble_values[3]),       # Number of averages
            'xincrement': float(preamble_values[4]), # Time difference between points
            'xorigin': float(preamble_values[5]),    # Start time of data
            'xreference': float(preamble_values[6]), # Reference time
            'yincrement': float(preamble_values[7]), # Vertical increment
            'yorigin': float(preamble_values[8]),    # Vertical offset
            'yreference': float(preamble_values[9])  # Vertical reference
        }
        
        return preamble

    def get_waveform_data(self, channel=None):
        """
        Query and return the screen waveform data from the specified channel.
        
        The function performs the following steps:
        1. Set the channel source (defaults to CH1 if not specified)
        2. Set the waveform reading mode to NORMAL
        3. Set the return format of the waveform data to BYTE
        4. Read the screen waveform data
        
        Args:
            channel (str, optional): The channel to get waveform data from. 
                                     Defaults to CH1 if None is provided.
        
        Returns:
            bytes: The raw waveform data in BYTE format
        """
        # If no channel is specified, default to CH1
        if channel is None:
            channel = self.CH1
            
        # Step 1: Set the channel source
        self.write(f":WAVeform:SOURce {channel}")
        
        # Step 2: Set the waveform reading mode to NORMAL
        self.write(":WAVeform:MODE NORM")
        
        # Step 3: Set the return format of the waveform data to BYTE/WORD/ASCII
        self.write(":WAVeform:FORMat ASCII")
        
        # Step 4: Read the screen waveform data
        # Note: Using read_raw() instead of ask() to get binary data
        self.write(":WAVeform:DATA?")
        waveform_data = self.device.read()
        
        return waveform_data
