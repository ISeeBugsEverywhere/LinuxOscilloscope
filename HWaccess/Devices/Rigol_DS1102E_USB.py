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
        self.t_name="Rigol DS1102E (USB)"
        self.idn = None
        self.mode = "NORM"
        self.CH1 = "CHAN1"
        self.CH2 = "CHAN2"
        self.CH_ARR = [self.CH1, self.CH2]
        self.CH_SIZE = 2
        pass

    def init_device(self, port:str, params):
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
        self.unlock_key()
        self.device.close()

    def stop(self):
        self.device.write(":STOP")

    #oscilloscope specific entries:
    def set_channels_mode(self, mode: str = "NORM"):
        '''
        Sets mode for CHAN1 and CHAN2

        :param str mode: NORM, RAW, MAX
        :return:
        '''
        a, _ = self.device.write(":WAV:POIN:MODE " + mode)
        if _ !=-1:
            self.mode = mode

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
        # TIME SECTION ===========================\n
        # Get the timescale

        :return:
        '''
        self.device.write(":TIM:SCAL?")
        timescale = float(self.device.read(20))
        return timescale

    def get_data_from_channel(self, channel, length=9000):
        '''
        Get arbitrary amount of data from specified channel

        :param str channel: CHAN1, CHAN2
        :param int length: default 9000
        :return array: array of data, already converted from binary form
        '''
        self.device.write(":WAV:DATA? " + channel)
        dataFromBuffer = self.device.read(length)
        data = np.frombuffer(dataFromBuffer, 'B')
        #:CHANnel < n >: SCALe < range >
        return data

    def get_channel_scale(self, CH: str):
        '''
        # Get the voltage scale CH1

        :return: voltscaleCH1 in Volts?
        '''
        self.device.write(":" + CH + ":SCAL?")
        voltscaleCH = float(self.device.read(20))
        return voltscaleCH

    def get_time_array(self, dataCHANNEL):
        '''

        :param array dataCHANNEL: array of data from channel
        :return: time, time Unit - time array and time dimension
        '''
        timescale = self.get_time_scale()
        timeoffset = self.get_time_offset()
        size_of_data = dataCHANNEL.size
        # Now, generate a time axis.
        time = np.linspace(timeoffset - 6 * timescale, timeoffset + 6 * timescale, num=len(dataCHANNEL))
        # this lets us to count in an offset of time, ensuring that the signal will be always
        # at the same position (will start)
        # Now, generate a time axis.  The scope display range is 0-600, with 300 being
        # time zero.
        # time = np.arange(-300.0 / 50 * timescale, 300.0 / 50 * timescale, timescale / 50.0)
        #  last working entry was:
        # time = np.arange(-(size_of_data/2) / 50 * timescale, (size_of_data/2) / 50 * timescale, timescale / 50.0)
        # If we generated too many points due to overflow, crop the length of time.
        if (time.size > dataCHANNEL.size):
            time = time[0:size_of_data:1]  # need to adopt to my needs// was [0:600:1].
        elif (time.size < dataCHANNEL.size):
            dataCHANNEL = dataCHANNEL[0:time.size:1]  # was [0:600:1]
            pass
        else:
            pass
        # tUnit section:
        if (time[599] < 1e-3):
            time = time * 1e6
            tUnit = "uS"
        elif (time[599] < 1):
            time = time * 1e3
            tUnit = "mS"
        else:
            tUnit = "S"

        return time, tUnit, dataCHANNEL

    def get_channel_position(self, CHANNEL):
        '''
        This function returns offset of specified channel

        :param str CHANNEL: channel
        :return:
        '''
        self.device.write(":" + CHANNEL + ":OFFS?")
        voltoffsetCH = float(self.device.read(20))
        return voltoffsetCH

    def run(self):
            self.device.write(":RUN")
            pass

    def unlock_key(self):
        self.device.write(":KEY:FORC")
        pass

    def get_data_points_from_channel(self, CH: str):
        '''

        :param str CH: channel
        :return: data form a channel, time_array, time_unit
        '''
        # Stop data acquisition:
        self.stop()
        # set wave data points mode to normal:
        self.set_channels_mode("NORM")
        data_array_from_channel = self.get_data_from_channel(CH, 9000)[10:]
        # Walk through the data, and map it to actual voltages
        # First invert the data (ya rly)
        dataCH = data_array_from_channel * -1 + 255
        # Voltage scale:
        voltscaleCH = self.get_channel_scale(CH)
        # Voltage offset
        voltoffsetCH = self.get_channel_position(CH)
        # Now, we know from experimentation that the scope display range is actually
        # 30-229.  So shift by 130 - the voltage offset in counts, then scale to
        # get the actual voltage.
        dataCH1 = (dataCH - 130.0 - voltoffsetCH / voltscaleCH * 25) / 25 * voltscaleCH
        # ==========================
        # Get a time scale:
        time_scale = self.get_time_scale()
        # get a time offset:
        time_offset = self.get_time_offset()
        # get time array:
        time_array, time_unit, dataCH2 = self.get_time_array(dataCH1)
        self.run()
        self.unlock_key()
        return dataCH2, time_array, time_unit
        pass

    def get_xy(self, CH:str):
        """

        :param CH: channel
        :return: data, time, time_unit, data will be in volts, time in time units, everything will be in lists
        """
        data, time, t_unit = self.get_data_points_from_channel(CH)
        return data.tolist(), time.tolist(), t_unit

    def ask(self, cmd:str):
        return self.device.ask(cmd)

    def write(self, cmd:str):
        self.device.write(cmd)
        pass

    def screenshot(self, fname="None", path="E:"):
        """
        writes a screenshot (*.BMP) into U:\ disk
        :return:
        """
        self.device.write(":HARDcopy")
        pass

    def _get_index_(self, letter):
        _letters_ = "abcdefghijklmnopqrstuvwxzy0123456789_<>"
        return _letters_.index(letter)

    def _get_diff_(self, a, b):
        sign = "+"
        d = a - b
        if d < 0:
            sign = "-"
        if d > 0:
            sign = "+"
        return abs(a-b), sign

    def save_all(self, fname="None", path="E:"):
        if len(fname) == 0:
            fname= "file"
        _letters_ = "abcdefghijklmnopqrstuvwxzy0123456789_"
        for i in fname:
            if i not in _letters_:
                fname = fname.replace(i, "")
        f_name = fname[0:8]
        # self.device.write(":KEY:MNU")
        self.device.write(":key:storage")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        self.device.write(":key:f1")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        i = 0
        for k in range(0, 4):
            self.device.write(":key:-func")
            time.sleep(0.1)
            time.sleep(0.5)
            self.screenshot()
            time.sleep(3)
        time.sleep(0.1)
        self.device.write(":key:+func")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        self.device.write(":key:func")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        self.device.write(":key:f4")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        self.device.write(":key:f2")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        for i in range(0,8):
            self.device.write(":key:f3")
            time.sleep(0.1)
            time.sleep(0.5)
            self.screenshot()
            time.sleep(3)
        curr_idx = 0
        next_idx = 0
        for i in f_name:
            next_idx = self._get_index_(i)
            step, sign = self._get_diff_(next_idx, curr_idx)
            if step == 0:
                self.device.write(":key:func")
                time.sleep(0.5)
                self.screenshot()
                time.sleep(3)
            else:
                if sign == "+":
                    for k in range(0, step):
                        self.device.write(":key:+func")
                        time.sleep(0.1)
                        time.sleep(0.5)
                        self.screenshot()
                        time.sleep(3)
                    self.device.write(":key:func")
                    time.sleep(0.5)
                    self.screenshot()
                    time.sleep(3)
                    curr_idx = next_idx
                elif sign == "-":
                    for k in range(0, step):
                        self.device.write(":key:-func")
                        time.sleep(0.1)
                        time.sleep(0.5)
                        self.screenshot()
                        time.sleep(3)
                    self.device.write(":key:func")
                    time.sleep(0.5)
                    self.screenshot()
                    time.sleep(3)
                    curr_idx = next_idx
            pass
        self.device.write(":key:f4")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        self.device.write(":key:mnu")
        time.sleep(0.1)
        time.sleep(0.5)
        self.screenshot()
        time.sleep(3)
        self.device.write(":key:run")
        pass