import os, sys
import platform

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.LinOsc import Ui_oscillWindow
import numpy as np
import math, time
import  traceback
from GUI.DevDlg import Dialog
import importlib.util
import importlib
from pyqtgraph import mkPen
import pyqtgraph as pg
from Scripts.vars import *
from Scripts.Threads import ContinuousUpdate
from Scripts.output_formatter import *
from Scripts.configparser import *
from PyQt5.QtWebKit import *

_new_line = os.linesep
try:
    from HWaccess.USBTMC_mod import USBTMC
except:
    USBTMC = None

GOM = None

R_THRAED = "Stop continuous\ndata acquisition"
START = "Get data from\nselected channel(s)"


class LOsc(QtWidgets.QMainWindow):
    def __init__(self):
        super(LOsc, self).__init__()
        self._new_line = _new_line
        self.ui = Ui_oscillWindow()
        self.ui.setupUi(self)
        self.setup_gui_fn()
        self._active = None # 0 - lxi, 1 - rs232, 2 - usbtmc, or strings lxi, rs232, usbtmc

        #threads:
        self._worker = None
        self._thread = QtCore.QThread(self)
        self._channels = {1:None, 2:None, 3:None, 4:None} #dictionry for channels
        self._gui_()
        self._signals_()
        self.OSCILLOSCOPE = None
        self._buttons = {1:self.ui.ch1_btn, 2:self.ui.ch2_btn, 3:self.ui.ch3_btn, 4:self.ui.ch4_btn}
        self._colors = [(255,255,0), (0,0,255), (0,128,0),(139,0,0)]
        self._data = {}
        self._loaded_cmds = []
        self.counter = 0
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
        self.ui.get_data_btn.clicked.connect(self.get_data_fn)
        self.ui.take_screenshot_btn.clicked.connect(self.screenshot_fn)
        self.ui.live_update_box.stateChanged.connect(self.live_update_changed)
        self.ui.dir_btn.clicked.connect(self.select_dir)
        self.ui.save_btn.clicked.connect(self.save_oscillogramme)
        self.ui.clear_btn.clicked.connect(self.clear_output)
        # stylesheets:
        self.ui.ch1_btn.clicked.connect(self.chfn)
        self.ui.ch2_btn.clicked.connect(self.chfn)
        self.ui.ch3_btn.clicked.connect(self.chfn)
        self.ui.ch4_btn.clicked.connect(self.chfn)
        # signals in the parameters tab:
        self.ui.idnButton.clicked.connect(self.get_idn)
        self.ui.rstButton.clicked.connect(self.rst_fn)
        self.ui.unlockButton.clicked.connect(self.unlock_fn)
        self.ui.executeButton.clicked.connect(self.execute_fn)
        self.ui.executeAllButton.clicked.connect(self.execute_all_fn)
        self.ui.cmdsButton.clicked.connect(self.get_cmds_fn)
        self.ui.clearButton.clicked.connect(self.clear_fn)
        self.ui.help_button.clicked.connect(lambda : self.show_help(True))
        self.ui.save_all_button.clicked.connect(self.save_all_fn)
        self.ui.rescan_ports_button.clicked.connect(self._get_ports_)
        self.ui.save_csv_button.clicked.connect(self.save_all_csv_fn)
        pass

    def save_all_csv_fn(self):
        fname = self.ui.name_all_box.text()
        path = self.ui.memory_box.currentText()
        self.OSCILLOSCOPE.save_all(fname, path)
        pass

    def save_all_fn(self):
        fname = self.ui.name_all_box.text()
        path = self.ui.memory_box.currentText()
        self.OSCILLOSCOPE.save_all(fname, path)
        time.sleep(2.0) # in seconds
        self.screenshot_fn()
        pass

    def show_help(self, swith=False):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "HelpFiles/lt.html"))
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        self.ui.webView.load(local_url)
        self.ui.webView.show()
        if swith:
            self.ui.tabWidget.setCurrentIndex(3)
        pass

    def rst_fn(self):
        self.OSCILLOSCOPE.reset()
        pass

    def unlock_fn(self):
        self.OSCILLOSCOPE.unlock_key()

    def execute_fn(self):
        try:
            cmd = self.ui.cmdsBox.currentText()
            if '?' in cmd:
                ret = self.OSCILLOSCOPE.ask(cmd)
                # self.ui.outputBox.appendPlainText(str(ret))
                self.append_output_paragraph(str(ret), 1)
            else:
                self.OSCILLOSCOPE.write(cmd)
            idx = self.ui.cmdsBox.findText(cmd)
            if idx == -1:
                self.ui.cmdsBox.addItem(cmd)
        except Exception as ex:
            self.append_output_paragraph(str(ex)+"\nGreičiausiai neteisinga komanda arba prietaisas atsijungė.", -1)

    def execute_all_fn(self):
        for i in self._loaded_cmds:
            if '?' in i:
                ret = self.OSCILLOSCOPE.ask(i)
                # self.ui.outputBox.appendPlainText(str(ret))
                self.append_output_paragraph(ret, 1)
            else:
                self.OSCILLOSCOPE.write(i)
                pass
            time.sleep(self.ui.sleep_time_box.value())
        pass

    def clear_fn(self):
        self.ui.outputBox.clear()
        pass

    def get_cmds_fn(self):
        dir_ = os.path.join(os.getcwd(), "CmdSets")
        dlg, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Select a file containing the commands', directory=dir_)
        if dlg is not None and dlg:
            with open(dlg, 'r') as d:
                lines = d.readlines()
                for i in lines:
                    self._loaded_cmds.append(i)
                self.ui.statusbar.showMessage('Loaded '+str(len(self._loaded_cmds))+' commands')
            pass
        pass

    def _check_btns(self):
        counter = 0
        for key, value in self._buttons.items():
            if value.isChecked():
                counter = counter + 1
        if counter == 0:
            self.ui.get_data_btn.setEnabled(False)



    def get_idn(self):
        name = self.OSCILLOSCOPE.get_name()
        # self.ui.outputBox.appendPlainText(name+self._new_line)
        self.append_output_paragraph(name, 1)

    def chfn(self):
        if self.ui.ch1_btn.isChecked():
            self.ui.ch1_btn.setStyleSheet("background-color: yellow")
            self.ui.ch1_comment.setEnabled(True)
            if not self.ui.get_data_btn.isEnabled():
                self.ui.get_data_btn.setEnabled(True)
        else:
            self.ui.ch1_btn.setStyleSheet("background-color: light grey")
            self.ui.ch1_comment.setEnabled(False)
            self.ui.ch1_comment.clear()
        if self.ui.ch2_btn.isChecked():
            self.ui.ch2_btn.setStyleSheet("background-color: blue")
            self.ui.ch2_comment.setEnabled(True)
            if not self.ui.get_data_btn.isEnabled():
                self.ui.get_data_btn.setEnabled(True)
        else:
            self.ui.ch2_btn.setStyleSheet("background-color: light grey")
            self.ui.ch2_comment.setEnabled(False)
            self.ui.ch2_comment.clear()
        if self.ui.ch3_btn.isChecked():
            self.ui.ch3_btn.setStyleSheet("background-color: green")
            self.ui.ch3_comment.setEnabled(True)
            if not self.ui.get_data_btn.isEnabled():
                self.ui.get_data_btn.setEnabled(True)
        else:
            self.ui.ch3_btn.setStyleSheet("background-color: light grey")
            self.ui.ch3_comment.setEnabled(False)
            self.ui.ch3_comment.clear()
        if self.ui.ch4_btn.isChecked():
            self.ui.ch4_btn.setStyleSheet("background-color: darkred")
            self.ui.ch4_comment.setEnabled(True)
            if not self.ui.get_data_btn.isEnabled():
                self.ui.get_data_btn.setEnabled(True)
        else:
            self.ui.ch4_btn.setStyleSheet("background-color: light grey")
            self.ui.ch4_comment.setEnabled(False)
            self.ui.ch4_comment.clear()
            pass
        self._check_btns()



    def clear_output(self):
        self.ui.infoText.clear()
        pass


    def select_dir(self):
        dlg = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Choose a directory", directory=os.getcwd()))
        if dlg is not None and dlg:
            self.ui.dir_label.setText(dlg)
            save_last_path(dlg)
            pass

    def fill_info_with_data(self):
        self.clear_output()
        # there goes everything:
        _o = get_o_d(self._data)
        _lo = len(_o)
        large_txt = ""
        for i in _o:
            large_txt = large_txt + str(i)+"<br>" # for html!
        self.append_html_paragraph(large_txt, 0, False)
        pass



    def save_oscillogramme(self):
        f_name= self.ui.file_name_entry.text()
        if 'csv' not in f_name:
            f_name = f_name+f'{self.counter:04}'+'.csv'
        else:
            f_name = f_name[:-4]+f'{self.counter:04}'+".csv"
        self.counter = self.counter + 1
        f_path = self.ui.dir_label.text()
        full_path = os.path.join(f_path, f_name)
        all_data = self.ui.infoText.toPlainText() # gets all data into one string
        all_data = all_data.replace(",", ";")
        w_data = ""
        if self.ui.ch1_comment.isEnabled():
            txt = self.ui.ch1_comment.text()
            all_data = all_data.replace("%COM"+str(self.OSCILLOSCOPE.CH1)+"%", txt)
        if self.ui.ch2_comment.isEnabled():
            txt = self.ui.ch2_comment.text()
            all_data = all_data.replace("%COM"+str(self.OSCILLOSCOPE.CH2)+"%", txt)
        if self.ui.ch3_comment.isEnabled():
            txt = self.ui.ch3_comment.text()
            all_data = all_data.replace("%COM"+str(self.OSCILLOSCOPE.CH3)+"%", txt)
        if self.ui.ch4_comment.isEnabled():
            txt = self.ui.ch4_comment.text()
            all_data = all_data.replace("%COM"+str(self.OSCILLOSCOPE.CH4)+"%", txt)
        w_data = all_data.replace("%TIME%", "S?")
        # writer it into a file:
        with open(full_path, 'w') as wrt:
            wrt.write(w_data)
            pass
        self.ui.saved_state_label.setText("SAVED: "+f_name)

    def live_update_changed(self):
        """
        Stops a thread, if live_update box becomes unchecked:
        :return:
        """
        if not self.ui.live_update_box.isChecked():
            if self._worker is not None and self._worker.ID == 1:
                self._worker.stop(True)
                self._worker = None
                # console("Thread stopped.")
                self._thread.exit(-27) # how about this? wrong again, leave it as is for a while
                # self._thread.terminate() # wrong approach here, need to fix it
                self.ui.get_data_btn.setText(START)
        pass

    def screenshot_fn(self):
        """
        takes a screenshot, but some oscilloscopes are missing this feature
        :return:

        """
        fname = self.ui.name_all_box.text()
        path = self.ui.memory_box.currentText()
        self.OSCILLOSCOPE.screenshot(fname, path)
        pass

    def _gui_(self):
        self.setWindowIcon(QtGui.QIcon('GUI/usb.png'))
        sys.path.append(os.getcwd() + "/HWaccess/Devices/") # stupid location for this entry
        self.ui.dir_label.setText(get_last_path())
        ips = get_last_ips()
        console(ips)
        self.ui.oscillographPlot.plotItem.showGrid(True, True, 1.0)
        for i in ips:
            if str(i) != '':
                self.ui.lxiCombo.addItem(str(i))
        self.show_help()

    def get_data_fn(self):

        """Gets a data and displays it"""
        # console("Gets a data")
        self._data = {}  # clears a dictionary
        if self.ui.get_data_btn.text() == R_THRAED:
            if self._worker is not None and self._worker.ID == 1:
                self._worker.stop(True)
                self._worker = None
                # console("Thread stopped.")
                self._thread.exit(-27) # how about this? wrong again, leave it as is for a while
                # self._thread.terminate() # wrong approach here, need to fix it
                self.ui.live_update_box.setChecked(False)
                self.ui.get_data_btn.setText(START)
        else:
            if self.ui.live_update_box.isChecked():
                self.ui.get_data_btn.setText(R_THRAED)
                if self._worker is not None and self._worker.ID == 1:
                    console("worker is not none")
                if self._worker is None:
                    # console("worker was NONE")
                    self._thread = QtCore.QThread(self)
                self._worker = ContinuousUpdate(self.OSCILLOSCOPE)
                channel = self.get_channels_array()
                sleep_t = self.ui.sleep_time_box.value()
                self._worker.init_params(channels=channel, sleep_time=sleep_t)
                self._worker.xy.connect(self.worker_xy)
                self._worker.progress.connect(self.worker_p)
                self._worker.moveToThread(self._thread)
                self._thread.started.connect(self._worker.run)
                self._thread.start()
            else:
                self.clear_plotted_items(self.ui.oscillographPlot)
                for index, btn in self._buttons.items():
                    if btn.isChecked():
                        if self._channels[index] is not None:
                            channel = self._channels[index]
                            y_array, x_array, t_Unit = self.OSCILLOSCOPE.get_xy(channel)
                            self._data[channel]=[x_array, y_array, t_Unit]
                            self.update_graph(self.ui.oscillographPlot, x_array, y_array, str(index), t_Unit, color=self._colors[index-1])
                self.fill_info_with_data()
                self.ui.saved_state_label.setText("NOT SAVED.")
                pass

    def worker_xy(self, y, x, x_unit, channel):
        index = list(self._channels.values()).index(channel)+1
        self.update_graph(self.ui.oscillographPlot, x, y, str(index), x_unit, color=self._colors[index - 1])
        self._data[channel] = [x, y, x_unit]
        self.fill_info_with_data()
        pass

    def worker_p(self, p):
        if p:
            self._data = {}
            pass

    def get_channels_array(self):
        channel = []
        for index, btn in self._buttons.items():
            if btn.isChecked():
                if self._channels[index] is not None:
                    channel.append(self._channels[index])
        return channel


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

    def _get_ports_(self):
        self.ui.rs232Combo.clear()
        ports = self.ui.rs232Widget.get_port_names()
        self.ui.rs232Combo.insertItems(0, [str(x.portName()) for x in ports])
        self.get_usbtmc_devices_fn()

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
        try:
            if "windows" in platform.system().lower():
                devices = USBTMC.get_devices()
                for i in devices:
                    self.ui.usbtmcCombo.addItem(str(devices))
        except Exception as ex:
            traceback.print_exc()
            self.append_html_paragraph(str(ex), -1, True)
            self.append_html_paragraph('Problems with USBTMC (python-usbtmc)', -1, True)
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
        if self._worker is not None and self._worker.ID == 1:
            self._worker.stop(True)
            self._worker = None
            # console("Thread stopped.")
            # self._thread.exit(-27)  # how about this? wrong again, leave it as is for a while
            self._thread.terminate() # wrong approach here, need to fix it
        if self.OSCILLOSCOPE is not None:
            self.OSCILLOSCOPE.close()
        if self._thread.isRunning():
            self._thread.terminate()
        while self._thread.isRunning():
            time.sleep(0.1)
        if not self._thread.isRunning():
            sys.exit(0)
        pass

    def get_port_parameters(self):
        params = self.ui.rs232Widget.return_serial_dict()
        if self.ui.lxiRadio.isChecked():
            port = self.ui.lxiCombo.currentText()
            return port, 0, params
        elif self.ui.rs232Radio.isChecked():
            port = self.ui.rs232Combo.currentText()
            pre = ''
            if 'linux' in platform.system().lower():
                pre='/dev/'
                print('linux')
            return pre+port, 1, params
        elif self.ui.usbtmcRadio.isChecked():
            port = self.ui.usbtmcCombo.currentText()
            return port, 2, params

    def connect_device_fn(self):
        try:
            if self.ui.connectButton.text() == "Connect":
                #self.collect_update_info()
                #dialog for the correct device:
                dlg_stat = False
                dialog = Dialog()
                if dialog.exec_():
                    dlg_stat=True
                    dvc = dialog.get_device()
                    global GOM
                    GOM = importlib.import_module(dvc)
                if dlg_stat:
                    self.trigger_device()
                    self.ui.connectButton.setText("Disconnect")
                    pass
            elif self.ui.connectButton.text() == "Disconnect":
                if self._worker is not None and self._worker.ID == 1:
                    self._worker.stop(True)
                    self._worker = None
                    # console("Thread stopped.")
                    # self._thread.exit(-27)  # how about this? wrong again, leave it as is for a while
                    self._thread.terminate()  # wrong approach here, need to fix it
                self.OSCILLOSCOPE = None
                self.ui.connectButton.setText("Connect")
                self._idnLabel("Not connected")
                self.setWindowTitle("Oscilloscope")
                self.ui.get_data_btn.setText(START)
        except Exception as ex:
            traceback.print_exc()
            self.append_html_paragraph(str(ex), -1, True)
            pass

    def trigger_device(self):
        try:
            port, status, params = self.get_port_parameters()
            self.OSCILLOSCOPE = GOM.Oscilloscope()
            # print(self.OSCILLOSCOPE.t_name)
            if status == 0:
                txt = self.ui.lxiCombo.currentText()
                idx = self.ui.lxiCombo.findText(txt)
                if idx == -1:
                    self.ui.lxiCombo.addItem(str(txt))
                # iterate over items, get them and write all of them into config file
                l = self.ui.lxiCombo.count()
                ips = ""
                for i in range(0, l):
                    ips = ips + self.ui.lxiCombo.itemText(i) + ","
                set_last_ips(ips)
                self.OSCILLOSCOPE.init_device(port, params)
                pass
            elif status == 1:
                self.OSCILLOSCOPE.init_device(port, params)

                pass
            elif status == 2:
                self.OSCILLOSCOPE.init_device(port, params)
            idn = self.OSCILLOSCOPE.get_name()
            self._idnLabel(idn)
            self.setWindowTitle(self.OSCILLOSCOPE.t_name+" : Oscilloscope")
            # continue with channel mapping:
            channels = self.OSCILLOSCOPE.CH_ARR
            count = self.OSCILLOSCOPE.CH_SIZE
            for i in range(1, count+1):
                self._channels[i] = channels[i-1]
                pass
            # print(self._channels, "CHANNELS")
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
            self.ui.tabWidget.setCurrentIndex(2)
        pass

    def append_output_paragraph(self, text, status=0):
        txt = str(text)
        html_red = '<font color="red">{x}</font>'
        html_black = '<font color="black">{x}</font>'
        html_magenta = '<font color="purple">{x}</font>'
        if status == 0: #regular info
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
            self.ui.outputBox.insertPlainText(self._new_line)
            self.ui.outputBox.setAlignment(QtCore.Qt.AlignLeft)
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
            self.ui.outputBox.insertHtml(html_black.replace('{x}', txt))
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
        elif status == 1: #some output from device
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
            self.ui.outputBox.insertPlainText(self._new_line)
            self.ui.outputBox.setAlignment(QtCore.Qt.AlignRight)
            # self.uinfoTextox.setFontWeight(QtGui.QFont.Bold)
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
            self.ui.outputBox.insertHtml(html_magenta.replace('{x}', txt))
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
        elif status == -1: #error
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
            self.ui.outputBox.insertPlainText(self._new_line)
            self.ui.outputBox.setAlignment(QtCore.Qt.AlignLeft)
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
            self.ui.outputBox.insertHtml(html_red.replace('{x}', txt))
            self.ui.outputBox.moveCursor(QtGui.QTextCursor.End)
        pass

    def _idnLabel(self, msg=None):
        if msg is not None:
            _str = "<html><head/><body><p><span style=\" font-weight:600;\">MSG</span></p></body></html>"
            self.ui.idnLabel.setText(_str.replace("MSG", str(msg)))
        pass

    def update_graph(self, graph:pg.PlotWidget, x, y, y_name, x_Unit, y_Unit='V', color=(255, 255, 102) ):
        """
        Updates a graph
        :param graph: plotWidget
        :param x: x dataset
        :param y: y dataset
        :param y_name: name (MUST)
        :param color: default: 255, 255, 102
        :return:
        """
        sizex = len(x)
        sizey=len(y)
        if sizex == sizey:
            dataItems =  graph.listDataItems()
            for i in dataItems:
                # console(i.name(), " ", y_name)
                if i is not None:
                    if i.name() == y_name:
                        graph.removeItem(i)
            cpen = mkPen(color=color, width=3)
            graph.plot(x,y, pen=cpen, name=y_name)
            graph.setLabel('bottom', "Time scale", units=str(x_Unit))
            graph.setLabel('left', "CH scale", units=str(y_Unit))
        else:
            console("Inequality", y_name, " ; ", sizex, " ; ", sizey)
            self.append_html_paragraph("Inequality: "+ str(y_name)+ " ; "+ str(sizex)+ " ; "+ str(sizey), -1, True)


    def clear_plotted_items(self, graph:pg.PlotWidget):
        dataItems = graph.listDataItems()
        for i in dataItems:
            # console(i.name(), " ", y_name)
            if i is not None:
                graph.removeItem(i)