import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.LinOsc import Ui_oscillWindow
from vxi11 import vxi11
from HWaccess.USBTMC import USBTMC
from PyQt5.QtCore import QIODevice

class LOsc(QtWidgets.QMainWindow):
    def __init__(self):
        super(LOsc, self).__init__()
        self.ui = Ui_oscillWindow()
        self.ui.setupUi(self)
        # radio signals:
        self.ui.lxiRadio.toggled.connect(self.lxi_state_fn)
        self.ui.rs232Radio.toggled.connect(self.rs232_state_fn)
        self.ui.usbtmcRadio.toggled.connect(self.usbtmc_state_fn)
        # quit actions:
        self.ui.quitButton.clicked.connect(self.quit_fn)
        self.ui.actionQuit_Ctrl_Q.triggered.connect(self.quit_fn)
        self.quitShortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Q'), self)
        self.quitShortcut.activated.connect(self.quit_fn)
        #
        self.setup_gui_fn()
        #
        self.ui.rs232Widget.returnPorts.connect(self.rescan_ports_fn)
        self.ui.rs232Combo.currentIndexChanged.connect(self.idx_fn)
        self.ui.rs232Widget.ui.comPortBox.currentIndexChanged.connect(self.idxfn)
        # devices
        self._rs232 = None
        self._lxi = None
        self._usbtmc = None
        self._active = None # 0 - lxi, 1 - rs232, 2 - usbtmc, or strings lxi, rs232, usbtmc
        self._new_line = os.linesep
        # buttons:
        self.ui.connectButton.clicked.connect(self.connect_device_fn)
        self.ui.ch1_btn.clicked.connect(self.checked_fn1)
        self.ui.ch2_btn.clicked.connect(self.checked_fn2)
        self.ui.ch3_btn.clicked.connect(self.checked_fn3)
        self.ui.ch4_btn.clicked.connect(self.checked_fn4)
        pass

    def checked_fn1(self):
        if not self.ui.ch1_btn.isChecked():
            self.ui.ch1_btn.setChecked(True)
            self.ui.ch2_btn.setChecked(False)
            self.ui.ch3_btn.setChecked(False)
            self.ui.ch4_btn.setChecked(False)
            print('ch1')
        elif self.ui.ch1_btn.isChecked():
            self.ui.ch2_btn.setChecked(False)
            self.ui.ch3_btn.setChecked(False)
            self.ui.ch4_btn.setChecked(False)

    def checked_fn2(self):
        if not self.ui.ch2_btn.isChecked():
            self.ui.ch1_btn.setChecked(False)
            self.ui.ch2_btn.setChecked(True)
            self.ui.ch3_btn.setChecked(False)
            self.ui.ch4_btn.setChecked(False)
            print('ch2')
        elif self.ui.ch2_btn.isChecked():
            self.ui.ch1_btn.setChecked(False)
            self.ui.ch3_btn.setChecked(False)
            self.ui.ch4_btn.setChecked(False)

    def checked_fn3(self):
        if not self.ui.ch3_btn.isChecked():
            self.ui.ch1_btn.setChecked(False)
            self.ui.ch2_btn.setChecked(False)
            self.ui.ch3_btn.setChecked(True)
            self.ui.ch4_btn.setChecked(False)
            print('ch3')
        elif self.ui.ch3_btn.isChecked():
            self.ui.ch2_btn.setChecked(False)
            self.ui.ch1_btn.setChecked(False)
            self.ui.ch4_btn.setChecked(False)

    def checked_fn4(self):
        if not self.ui.ch4_btn.isChecked():
            self.ui.ch1_btn.setChecked(False)
            self.ui.ch2_btn.setChecked(False)
            self.ui.ch3_btn.setChecked(False)
            self.ui.ch4_btn.setChecked(True)
            print('ch4')
        elif self.ui.ch4_btn.isChecked():
            self.ui.ch2_btn.setChecked(False)
            self.ui.ch3_btn.setChecked(False)
            self.ui.ch1_btn.setChecked(False)

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
        self.get_usbtmc_devices()
        pass

    def get_usbtmc_devices_fn(self):
        try:
            self.ui.usbtmcCombo.clear()
            mypath = "/dev"
            for f in os.listdir(mypath):
                if f.startswith('usbtmc'):
                    self.ui.usbtmcCombo.addItem(mypath + "/" + f)
        except Exception as ex:
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

    def connect_device_fn(self):
        if self.ui.lxiRadio.isChecked():
            ip = self.ui.lxiCombo.currentText()
            self._lxi = vxi11.Instrument(ip)
            self._lxi.open()
            idn = self._lxi.ask('*idn?')
            self.ui.idnLabel.setText(str(idn))
            self._active = 'lxi'
            pass
        elif self.ui.rs232Radio.isChecked():
            # self._rs232 = self.ui.rs232Widget.getSerialPort()
            # status = self._rs232.open(QIODevice.ReadWrite)
            # if status:
            #     pass
            pass
        elif self.ui.usbtmcRadio.isChecked():
            self._usbtmc = USBTMC(self.ui.usbtmcCombo.currentText())
            self._usbtmc.set_encoding(self.ui.usbtmc_encoding_box.currentText())
            self._usbtmc.set_errors_behavior(self.ui.usbtmc_errors_box.currentText())
            idn = self._usbtmc.ask('*idn?')
            self.ui.idnLabel.setText(str(idn))
        pass

    def append_html_paragraph(self, text, status=0):
        txt = str(text)
        html_red = '<font color="red">{x}</font>'
        html_black = '<font color="black">{x}</font>'
        html_magenta = '<font color="purple">{x}</font>'
        if status == 0:
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertPlainText(self._new_line)
            self.ui.infoText.setAlignment(QtCore.Qt.AlignLeft)
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertHtml(html_black.replace('{x}', txt))
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
        elif status == 1:
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertPlainText(self._new_line)
            self.ui.infoText.setAlignment(QtCore.Qt.AlignRight)
            # self.uinfoTextox.setFontWeight(QtGui.QFont.Bold)
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertHtml(html_magenta.replace('{x}', txt))
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
        elif status == -1:
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertPlainText(self._new_line)
            self.ui.infoText.setAlignment(QtCore.Qt.AlignLeft)
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
            self.ui.infoText.insertHtml(html_red.replace('{x}', txt))
            self.ui.infoText.moveCursor(QtGui.QTextCursor.End)
        pass