from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
import time

class ContinuousUpdate(QObject):
    def __init__(self):
        super(ContinuousUpdate, self).__init__()
        self.require_stop=False
        pass

    @pyqtSlot()
    def run(self):
        while not self.require_stop:
            print('RUNNING thread, sleep for 5 sec')
            time.sleep(5)
        print("Exiting the current thread")

    @pyqtSlot()
    def stop(self, p:bool):
        self.require_stop = p
        pass