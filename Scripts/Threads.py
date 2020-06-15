from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
import time, os, sys

class ContinuousUpdate(QObject):
    xy = pyqtSignal(list, list, str, str) # y, x, t_unit, channel number/name
    progress = pyqtSignal(bool)
    def __init__(self, oscilloscope):
        super(ContinuousUpdate, self).__init__()
        self.require_stop=False
        self.ID = 1
        self.OSCILLOSCOPE = oscilloscope
        self.sleep_time = 1
        self.channels = [] # array of channels, but there has to be actual channels
        pass

    def init_params(self, channels=None, sleep_time=1):
        if channels is not None:
            self.channels = channels
        self.sleep_time = sleep_time
        pass

    @pyqtSlot()
    def run(self):
        while not self.require_stop:
            for i in self.channels:
                y, x, x_unit = self.OSCILLOSCOPE.get_xy(i)
                self.xy.emit(y, x, x_unit, i)
            self.progress.emit(True)
            time.sleep(self.sleep_time)
        print("Exiting the current thread")
        # sys.exit(0)

    @pyqtSlot()
    def stop(self, p:bool):
        self.require_stop = p
        pass