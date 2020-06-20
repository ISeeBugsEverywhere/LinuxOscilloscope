import platform

from PyQt5 import QtWidgets, QtGui
import sys, os
from GUI.Device_Dialog import Ui_Dialog

import glob

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._setup_()

    def _setup_(self):
        """
        Get all device classes:
        :return:
        """
        if "windows" in platform.system().lower():
            files = glob.glob("HWaccess\Devices\*.py")
            dvces = []
            for i in files:
                device = i.split("/")[-1][:-3]
                dvces.append(device)
                pass
            dvces.sort() # in-place sorted
            for a in dvces:
                self.ui.deviceBox.addItem(a)
            pass
        else:
            files = glob.glob("HWaccess/Devices/*.py")
            dvces = []
            for i in files:
                device = i.split("/")[-1][:-3]
                dvces.append(device)
                pass
            dvces.sort()  # in-place sorted
            for a in dvces:
                self.ui.deviceBox.addItem(a)
            pass

    def get_device(self):
        return self.ui.deviceBox.currentText()
        pass

