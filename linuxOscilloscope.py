import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.LinOsc import Ui_oscillWindow
from vxi11 import vxi11
from HWaccess.USBTMC import USBTMC
from PyQt5.QtCore import QIODevice
import numpy as np
import math
import  traceback
from GUI.DevDlg import Dialog
import importlib.util

class LOsc(QtWidgets.QMainWindow):
    def __init__(self):
        super(LOsc, self).__init__()
        self.ui = Ui_oscillWindow()
        self.ui.setupUi(self)
        self.setup_gui_fn()
        self._active = None # 0 - lxi, 1 - rs232, 2 - usbtmc, or strings lxi, rs232, usbtmc
        self._new_line = os.linesep
        self._active_channels = []
        self._vertical_cmds_dict = {}
        self._horizontal_cmds_dict = {}
        # will executed before real getting commands:
        self._prep_h_cmds=[]
        self._prep_y_cmds=[]
        #threads:
        self._worker = None
        self._thread = QtCore.QThread()
        self._channels = {1:None, 2:None, 3:None, 4:None} #dictionry for channels
        self._y_expr = None
        self._h_expr = None
        self._gui_()
        self._signals_()
        self.OSCILLOSCOPE = None
        pass

    def _signals_(self):
        # radio signals:
        self.ui.lxiRadio.toggled.connect(self.lxi_state_fn)
        self.ui.rs232Radio.toggled.connect(self.rs232_state_fn)
        self.ui.usbtmcRadio.toggled.connect(self.usbtmc_state_fn)
        # quit actions:
        self.ui.quitButton.clicked.connect(self.quit_fn)
        self.ui.actionQuit_Ctrl_Q.triggered.connect(self.quit_fn)
        self.quitShortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Q'), self)
        self.quitShortcut.activated.connect(self.quit_fn)
        self.ui.rs232Widget.returnPorts.connect(self.rescan_ports_fn)
        self.ui.rs232Combo.currentIndexChanged.connect(self.idx_fn)
        self.ui.rs232Widget.ui.comPortBox.currentIndexChanged.connect(self.idxfn)
        # buttons:
        self.ui.connectButton.clicked.connect(self.connect_device_fn)
        self.ui.ch1_btn.clicked.connect(self.checked_fn1)
        self.ui.ch2_btn.clicked.connect(self.checked_fn2)
        self.ui.ch3_btn.clicked.connect(self.checked_fn3)
        self.ui.ch4_btn.clicked.connect(self.checked_fn4)
        self.ui.get_data_btn.clicked.connect(self.get_data_fn)
        self.ui.take_screenshot_btn.clicked.connect(self.screenshot_fn)
        pass

    def screenshot_fn(self):
        """
        takes a screenshot, but some oscilloscopes are missing this feature
        :return:
        """
        pass

    def _gui_(self):
        self.setWindowIcon(QtGui.QIcon('GUI/usb.png'))
        sys.path.append(os.getcwd() + "/HWaccess/Devices/") # stupid location for this entry
        pass

    def get_data_fn(self):
        pass







    def fill_channels_fn(self):
        dict_len = len(self._channels)
        for key, value in self._channels.items():
            print(key, value)
            if value is not None:
                self._active_channels.append(value)
                pass
        pass




    def checked_fn1(self):
        try:
            if not self.ui.ch1_btn.isChecked():
                ch = self._channels[1]
                self._active_channels.remove(ch)
                pass
                # print('ch1')
                # self._channels.remove('ch1')
            elif self.ui.ch1_btn.isChecked():
                ch = self._channels[1]
                self._active_channels.append(ch)
                # self._channels.append('ch1')
                # print('ch1 ...')
                pass
        except Exception as ex:
            print(str(ex))
            pass

    def checked_fn2(self):
        try:
            if not self.ui.ch2_btn.isChecked():
                ch = self._channels[2]
                self._active_channels.remove(ch)
                print('ch2')
            elif self.ui.ch2_btn.isChecked():
                ch = self._channels[2]
                self._active_channels.append(ch)
                print('ch2 ...')
        except Exception as ex:
            print(str(ex))
            pass

    def checked_fn3(self):
        try:
            if not self.ui.ch3_btn.isChecked():
                ch = self._channels[3]
                self._active_channels.remove(ch)
                print('ch3')
            elif self.ui.ch3_btn.isChecked():
                ch = self._channels[3]
                self._active_channels.append(ch)
                print('ch3 ...')
        except Exception as ex:
            print(str(ex))
            pass

    def checked_fn4(self):
        try:
            if not self.ui.ch4_btn.isChecked():
                ch = self._channels[4]
                self._active_channels.remove(ch)
                print('ch4')
            elif self.ui.ch4_btn.isChecked():
                ch = self._channels[4]
                self._active_channels.append(ch)
                print('ch4 ...')
        except Exception as ex:
            print(str(ex))
            pass

    def setup_gui_fn(self):
        self.update_ports_fn()
        pass

    def update_ports_fn(self):
        ports = self.ui.rs232Widget.get_port_names()
        self.ui.rs232Combo.insertItems(0, [str(x.portName()) for x in ports])
        self.get_usbtmc_devices_fn()
        pass

    def rescan_ports_fn(self, ports):
        self.ui.rs232Combo.clear()
        self.ui.rs232Combo.insertItems(0, [str(x.portName()) for x in ports])
        self.get_usbtmc_devices_fn()
        pass

    def get_usbtmc_devices_fn(self):
        try:
            self.ui.usbtmcCombo.clear()
            mypath = "/dev"
            for f in os.listdir(mypath):
                if f.startswith('usbtmc'):
                    self.ui.usbtmcCombo.addItem(mypath + "/" + f)
        except Exception as ex:
            self.append_html_paragraph(str(ex), -1, True)
            self.append_html_paragraph('There aren\'t any USBTMC devices or you are running on Windows machine', -1, True)
            pass

    def lxi_state_fn(self):
        if self.ui.lxiRadio.isChecked():
            self.ui.lxiCombo.setEnabled(True)
            self.ui.rs232Combo.setEnabled(False)
            self.ui.usbtmcCombo.setEnabled(False)
            pass
        pass

    def rs232_state_fn(self):
        if self.ui.rs232Radio.isChecked():
            self.ui.lxiCombo.setEnabled(False)
            self.ui.rs232Combo.setEnabled(True)
            self.ui.usbtmcCombo.setEnabled(False)
            pass

    def usbtmc_state_fn(self):
        if self.ui.usbtmcRadio.isChecked():
            self.ui.lxiCombo.setEnabled(False)
            self.ui.rs232Combo.setEnabled(False)
            self.ui.usbtmcCombo.setEnabled(True)
            pass
        pass

    def idxfn(self, index):
        self.ui.rs232Combo.setCurrentIndex(index)
        pass

    def idx_fn(self, index):
        # self.ui.com_params_widget.ui.comPortBox.setCurrentIndex(index)
        self.ui.rs232Widget.ui.comPortBox.setCurrentIndex(index)
        pass

    def quit_fn(self):
        sys.exit(0)
        pass

    def get_port_parameters(self):
        params = self.ui.rs232Widget.return_serial_dict()
        if self.ui.lxiRadio.isChecked():
            port = self.ui.lxiCombo.currentText()
            return port, 0, params
        elif self.ui.rs232Radio.isChecked():
            port = self.ui.rs232Combo.currentText()
            return port, 1, params
        elif self.ui.usbtmcRadio.isChecked():
            port = self.ui.usbtmcCombo.currentText()
            return port, 2, params

    def connect_device_fn(self):
        try:
            self.collect_update_info()
            #dialog for the correct device:
            dialog = Dialog()
            if dialog.exec_():
                dvc = dialog.get_device()
                print(dvc)
                _m_dvc = __import__(dvc)
                port, status, params = self.get_port_parameters()
                self.OSCILLOSCOPE = _m_dvc.Oscilloscope()
                print(self.OSCILLOSCOPE.t_name)
                if status == 0:
                    self.OSCILLOSCOPE.init_device(port, params)
                elif status == 1:
                    self.OSCILLOSCOPE.init_device(port, params)
                elif status == 2:
                    self.OSCILLOSCOPE.init_device(port, params)
                idn  = self.OSCILLOSCOPE.get_name()
                self.ui.idnLabel.setText(idn)
                print (idn)
        except Exception as ex:
            traceback.print_exc()
            self.append_html_paragraph(str(ex), -1, True)
            pass

    def append_html_paragraph(self, text, status=0, show = False):
        txt = str(text)
        html_red = '<font color="red">{x}</font>'
        html_black = '<font color="black">{x}</font>'
        html_magenta = '<font color="purple">{x}</font>'
        if status == 0: #regular info
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertPlainText(self._new_line)
            self.ui.infoText.setAlignment(QtCore.Qt.AlignLeft)
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertHtml(html_black.replace('{x}', txt))
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
        elif status == 1: #some output from device
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertPlainText(self._new_line)
            self.ui.infoText.setAlignment(QtCore.Qt.AlignRight)
            # self.uinfoTextox.setFontWeight(QtGui.QFont.Bold)
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertHtml(html_magenta.replace('{x}', txt))
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
        elif status == -1: #error
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertPlainText(self._new_line)
            self.ui.infoText.setAlignment(QtCore.Qt.AlignLeft)
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertHtml(html_red.replace('{x}', txt))
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
        if show:
            self.ui.tabWidget.setCurrentIndex(3)
        pass

    def _idnLabel(self, msg=None):
        if msg is not None:
            _str = "<html><head/><body><p><span style=\" font-weight:600;\">MSG</span></p></body></html>"
            self.ui.idnLabel.setText(_str.replace("MSG", str(msg)))
        pass