from PyQt5 import QtWidgets, QtGui
import sys
from GUI.Device_Dialog import Ui_Dialog

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def _setup_(self):
        pass

    def exit_fn(self):
        sys.exit(0)

    def connect_fn(self):
        return "DeVICE"


    def signals(self):
        self.ui.cancelButton.clicked.connect(self.exit_fn)
        self.ui.connectButton.clicked.connect(self.connect_fn)
