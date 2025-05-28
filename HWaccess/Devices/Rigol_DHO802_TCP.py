import os
import sys
import numpy as np
import math
# from HWaccess.USBTMC import USBTMC # -- for USBTMC
# from HWaccess.VISADevice import VISADevice
# import pyvisa as visa
import vxi11 # -- for LXI instruments

class Oscilloscope:
    """
    Rigol DHO 802 wrapper
    """
    def __init__(self):
        # ====================
        # THESE ATTRIBUTES MUST BE IMPLEMENTED:
        self.device = None
        self.t_name="Rigol DHO802 (TCP)"
        self.idn = None
        self.mode = "NORM"
        self.CH1 = "CHAN1"
        self.CH2 = "CHAN2"
        self.CH_ARR = [self.CH1, self.CH2]
        self.CH_SIZE = 2
        # === END OF NECESSARY ATTRIBUTES ==========
        # BELOW any attribute can be implemented
        pass
    # ============================================================
    # FROM HERE:
    # ALL THESE METHODS MUST BE IMPLEMENTED:
    # ============================================================
    def init_device(self, port:str, params):
        self.device = vxi11.Instrument(port)
        pass

    def get_name(self):
        r = self.device.ask('*IDN?')
        return r
        pass

    def reset(self):
        a = self.device.write("*RST")
        pass

    def unlock_key(self):
        pass

    def save_all(self,fname, path):
        pass

    def screenshot(self,fname, path):
        pass

    def ask(self, cmd:str, length=4000):
        resp = self.device.ask(cmd)
        return resp

    def write(self, cmd:str):
        r = self.device.write(cmd)
        return r # grąžina įrašytų baitų kiekį
    
    def close(self):
        """Close the device connection."""
        if self.device is not None:
            self.device.close()
            self.device = None
        pass

    def get_xy(self, channel:str):
        """Get X and Y data from the specified channel."""
        time, volts, unit = self.get_waveform(channel)
        return volts, time, unit
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

    def get_waveform(self, channel:str):
        """Get waveform data from specified channel.
        
        Args:
            channel (str): Channel name (CHAN1, CHAN2, etc.)
            
        Returns:
            tuple: (time_values, voltage_values, time_unit) arrays
        """
        # Stop the oscilloscope to read data
        self.write(":STOP")
        
        # Configure waveform reading
        self.write(":WAV:SOUR " + channel)
        self.write(":WAV:MODE RAW")
        self.write(":WAV:FORM ASC")
        
        # Set memory depth to 10k
        self.write(":ACQ:MDEP 10K")
        
        # Set reading points
        self.write(":WAV:STAR 1")
        self.write(":WAV:STOP 10000")
        
        # Get waveform parameters
        preamble = self.ask(":WAV:PRE?")
        pre_params = preamble.split(',')
        
        # Parse preamble parameters
        x_increment = float(pre_params[4])  # Time difference between two adjacent points
        x_origin = float(pre_params[5])     # Start time of waveform data
        y_increment = float(pre_params[7])  # Voltage step between two adjacent points
        y_origin = float(pre_params[8])     # Vertical offset relative to trigger position
        y_ref = float(pre_params[9])        # Vertical reference position
        
        # Get waveform data
        data_str = self.ask(":WAV:DATA?")
        
        # Convert string data to numerical values
        raw_data = []
        for f in data_str.split(','):
            try:
                raw_data.append(float(f))
            except ValueError:
                a, b = [f[0:13], f[13:]]
                raw_data.append(float(a))
                raw_data.append(float(b))
                
        # raw_data = [float(val) for val in data_str.split(',')]
        
        # Calculate time and voltage values
        time_values = [x_origin + i * x_increment for i in range(len(raw_data))]
        # voltage_values = [(val - y_ref) * y_increment + y_origin for val in raw_data]
        voltage_values = raw_data
        # Return the oscilloscope to run state
        self.write(":RUN")
        
        return time_values, voltage_values, 's'
    
