import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.LinOsc import Ui_oscillWindow
from vxi11 import vxi11
from HWaccess.USBTMC import USBTMC
from PyQt5.QtCore import QIODevice
import numpy as np
import math

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
        self._active_channels = []
        self._vertical_cmds_dict = {}
        self._horizontal_cmds_dict = {}
        #threads:
        self._worker = None
        self._thread = QtCore.QThread()
        # buttons:
        self.ui.connectButton.clicked.connect(self.connect_device_fn)
        self.ui.ch1_btn.clicked.connect(self.checked_fn1)
        self.ui.ch2_btn.clicked.connect(self.checked_fn2)
        self.ui.ch3_btn.clicked.connect(self.checked_fn3)
        self.ui.ch4_btn.clicked.connect(self.checked_fn4)
        self.ui.execute_scpi_btn.clicked.connect(self.exec_scpi_fn)
        self._channels = {1:None, 2:None, 3:None, 4:None} #dictionry for channels
        self.ui.get_vertical_cmds_btn.clicked.connect(self.get_v_cmds_fn)
        self.ui.get_h_cmds_btn.clicked.connect(self.get_h_cmds_fn)
        self.collect_update_info()
        self._y_expr = None
        self._h_expr = None
        self.ui.test_fn_btn.clicked.connect(self._test_eval_fn)
        self.ui.get_data_btn.clicked.connect(self.get_data_fn)
        pass

    def get_data_fn(self):
        try:
            y_data = self.get_vertical_data('chan1')
            x_data = self.get_horizontal_data()
            print('##########################')
            print(y_data)
            print('##########################')
            print(x_data)
            print('##########################')
        except Exception as ex:
            print(str(ex), 'get data fn')
        pass

    def _test_eval_fn(self):
        '''
        It works, just we ned to use self. before any variable
        :return:
        '''
        exp = eval(self.ui.vertical_expression.text())
        print(exp)
        pass

    def get_vertical_data(self, channel:str):
        if self._active == 'lxi' and self._lxi is not None:
            for key, value in self._vertical_cmds_dict:
                print(key, value)
                key = self._lxi.ask(value.replace('{x}', channel))
        elif self._active == 'usbtmc' and self._lxi is not None:
            for key, value in self._vertical_cmds_dict:
                print(key, value)
                key = self._usbtmc.ask(value.replace('{x}', channel))
        elif self._active == 'rs232' and self._lxi is not None:
            for key, value in self._vertical_cmds_dict:
                print(key, value)
                print('NOT IMPLEMENTED YET!')
        else:
            print('-30 mark - no recognisable device!')
            sys.exit(-30)
        y_data = eval(self._y_expr)
        return y_data
        pass

    def get_horizontal_data(self):
        if self._active == 'lxi' and self._lxi is not None:
            for key, value in self._horizontal_cmds_dict:
                print(key, value)
                key = self._lxi.ask(value)
        elif self._active == 'usbtmc' and self._lxi is not None:
            for key, value in self._horizontal_cmds_dict:
                print(key, value)
                key = self._usbtmc.ask(value)
        elif self._active == 'rs232' and self._lxi is not None:
            for key, value in self._horizontal_cmds_dict:
                print(key, value)
                print('NOT IMPLEMENTED YET!')
        else:
            print('-30 mark - no recognisable device!')
            sys.exit(-30)
        x_data = eval(self._h_expr)
        return x_data
        pass

    def get_v_cmds_fn(self):
        # food = 'bread'
        # vars(self)[food] = 'data'
        # print('vars(): ', vars(self))
        # easier access is this way:
        # setattr(self, 'bread', 'easier access')
        # print(getattr(self, 'bread'))
        entry_splitter = ':='
        fname, _ = QtWidgets.QFileDialog().getOpenFileName(self, caption='Open V-scale commands')
        if fname:
            print('fname', fname)
            f = open(fname, 'r')
            lines = f.readlines()
            content = [x.strip() for x in lines]
            cmds = content
            for i in cmds:
                var, cmd = i.split(entry_splitter)
                self._vertical_cmds_dict[var]=cmd
                setattr(self, var, 5)
                pass
        if len(self.ui.vertical_expression.text()) > 5:
            self._y_expr = self.ui.vertical_expression.text()
        pass

    def get_h_cmds_fn(self):
        # setattr(self, 'bread', 'easier access')
        # print(getattr(self, 'bread'))
        entry_splitter = ':='
        fname, _ = QtWidgets.QFileDialog().getOpenFileName(self, caption='Open H-scale commands')
        if fname:
            print('fname', fname)
            f = open(fname, 'r')
            lines = f.readlines()
            content = [x.strip() for x in lines]
            cmds = content
            for i in cmds:
                var, cmd = i.split(entry_splitter)
                self._horizontal_cmds_dict[var] = cmd
                setattr(self, var, None)
                pass
        if len(self.ui.horizontal_expression.text()) > 5:
            self._y_expr = self.ui.horizontal_expression.text()

    def collect_update_info(self):
        channels_string = self.ui.channels_names_box.text()
        if channels_string is not None and len(channels_string) >= 2:
            splitted = channels_string.split(',')
            l = len(splitted)
            self.append_html_paragraph(str(l)+' : given number of channels')
            for i in range(0, l):
                self._channels[i+1] = splitted[i]
            pass
        self.fill_channels_fn()

    def fill_channels_fn(self):
        dict_len = len(self._channels)
        for key, value in self._channels.items():
            print(key, value)
            if value is not None:
                self._active_channels.append(value)
                pass
        pass

    def exec_scpi_fn(self):
        print('execute scpi cmd ...')
        scpi_cmd = self.ui.scpi_cmd_box.currentText()
        if self._active == 'lxi':
            pass
        elif self._active == 'usbtmc':
            print(' on usbtmc ...')
            self._usbtmc.write(scpi_cmd)
        elif self._active == 'rs232':
            pass
        pass

    def checked_fn1(self):
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

    def checked_fn2(self):
        if not self.ui.ch2_btn.isChecked():
            ch = self._channels[2]
            self._active_channels.remove(ch)
            print('ch2')
        elif self.ui.ch2_btn.isChecked():
            ch = self._channels[2]
            self._active_channels.append(ch)
            print('ch2 ...')

    def checked_fn3(self):
        if not self.ui.ch3_btn.isChecked():
            ch = self._channels[3]
            self._active_channels.remove(ch)
            print('ch3')
        elif self.ui.ch3_btn.isChecked():
            ch = self._channels[3]
            self._active_channels.append(ch)
            print('ch3 ...')

    def checked_fn4(self):
        if not self.ui.ch4_btn.isChecked():
            ch = self._channels[4]
            self._active_channels.remove(ch)
            print('ch4')
        elif self.ui.ch4_btn.isChecked():
            ch = self._channels[4]
            self._active_channels.append(ch)
            print('ch4 ...')

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
            print('There aren\'t any USBTMC devices or you are running on Windows machine')
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
        try:
            self.collect_update_info()
            if self.ui.lxiRadio.isChecked():
                ip = self.ui.lxiCombo.currentText()
                self._lxi = vxi11.Instrument(ip)
                self._lxi.open()
                idn = self._lxi.ask('*idn?')
                self.ui.idnLabel.setText(str(idn))
                self._active = 'lxi'
                pass
            elif self.ui.rs232Radio.isChecked():
                self._rs232 = self.ui.rs232Widget.getSerialPort()
                status = self._rs232.open(QIODevice.ReadWrite)
                if status:
                    self._rs232.write(bytes('*idn?', encoding='ascii'))
                    idn = self._rs232.read(300)
                    self.ui.idnLabel.setText(str(idn))
                else:
                    self.append_html_paragraph('RS232 was opened: '+str(status), -1, True)
            elif self.ui.usbtmcRadio.isChecked():
                self._usbtmc = USBTMC(self.ui.usbtmcCombo.currentText())
                self._usbtmc.set_encoding(self.ui.usbtmc_encoding_box.currentText())
                self._usbtmc.set_errors_behavior(self.ui.usbtmc_errors_box.currentText())
                idn = self._usbtmc.ask_string('*idn?')
                self.ui.idnLabel.setText(str(idn))
                self._active = 'usbtmc'
            pass
        except Exception as ex:
            self.append_html_paragraph(str(ex), -1, True)
            pass

    def append_html_paragraph(self, text, status=0, show = False):
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
        if show:
            self.ui.tabWidget.setCurrentIndex(3)
        pass