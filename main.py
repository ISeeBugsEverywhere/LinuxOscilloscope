#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from linuxOscilloscope import LOsc


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    try:
        app.setStyle('Oxygen')
    except:
        pass
    window = LOsc()
    window.show()
    sys.exit(app.exec_())