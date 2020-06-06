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
        files = glob.glob("HWaccess/Devices/*.py")
        for i in files:
            device = i.split("/")[-1][:-3]
            self.ui.deviceBox.addItem(device)
        pass

    def get_device(self):
        return self.ui.deviceBox.currentText()
        pass

