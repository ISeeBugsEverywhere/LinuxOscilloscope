import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.LinOsc import Ui_oscillWindow
import numpy as np
import math
import  traceback
from GUI.DevDlg import Dialog
import importlib.util
import importlib
from pyqtgraph import mkPen
import pyqtgraph as pg
from Scripts.vars import *
from Scripts.Threads import ContinuousUpdate
from Scripts.output_formatter import *

GOM = None

class LOsc(QtWidgets.QMainWindow):
    def __init__(self):
        super(LOsc, self).__init__()
        self.ui = Ui_oscillWindow()
        self.ui.setupUi(self)
        self.setup_gui_fn()
        self._active = None # 0 - lxi, 1 - rs232, 2 - usbtmc, or strings lxi, rs232, usbtmc
        self._new_line = os.linesep
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
        pass

    def select_dir(self):
        dlg = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Choose a directory", directory=os.getcwd()))
        if dlg is not None and dlg:
            self.ui.dir_label.setText(dlg)
            pass

    def save_oscillogramme(self):
        f_name= self.ui.file_name_entry.text()
        if 'csv' not in f_name:
            f_name = f_name+'.csv'
        f_path = self.ui.dir_label.text()
        full_path = os.path.join(f_path, f_name)
        print(full_path)
        # there goes everything:
        #
        pass

    def live_update_changed(self):
        if not self.ui.live_update_box.isChecked():
            if self._worker is not None and self._worker.ID == 1:
                self._worker.stop(True)
                self._worker = None
                # console("Thread stopped.")
                self._thread.exit(-27) # how about this? wrong again, leave it as is for a while
                # self._thread.terminate() # wrong approach here, need to fix it
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
        """Gets a data and displays it"""
        console("Gets a data")
        self._data = {} # clears a dictionary
        if self.ui.live_update_box.isChecked():
            console("Threading ...")
            if self._worker is not None and self._worker.ID == 1:
                console("worker is not none")
            if self._worker is None:
                console("worker was NONE")
                self._thread = QtCore.QThread(self)
            self._worker = ContinuousUpdate(self.OSCILLOSCOPE)
            channel = self.get_channels_array()
            sleep_t = self.ui.sleep_time_box.value()
            self._worker.init_params(channels=channel, sleep_time=sleep_t)
            self._worker.xy.connect(self.worker_xy)
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
            pass

    def worker_xy(self, y, x, x_unit, channel):
        index = list(self._channels.values()).index(channel)+1
        self.update_graph(self.ui.oscillographPlot, x, y, str(index), x_unit, color=self._colors[index - 1])
        pass

    def get_channels_array(self):
        channel = []
        for index, btn in self._buttons.items():
            if btn.isChecked():
                if self._channels[index] is not None:
                    channel.append(self._channels[index])
        return channel

    def check_channel_btn(self):
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
        except Exception as ex:
            traceback.print_exc()
            self.append_html_paragraph(str(ex), -1, True)
            pass

    def trigger_device(self):
        try:
            port, status, params = self.get_port_parameters()
            self.OSCILLOSCOPE = GOM.Oscilloscope()
            print(self.OSCILLOSCOPE.t_name)
            if status == 0:
                self.OSCILLOSCOPE.init_device(port, params)
            elif status == 1:
                self.OSCILLOSCOPE.init_device(port, params)
            elif status == 2:
                self.OSCILLOSCOPE.init_device(port, params)
            idn = self.OSCILLOSCOPE.get_name()
            self._idnLabel(idn)
            # continue with channel mapping:
            channels = self.OSCILLOSCOPE.CH_ARR
            count = self.OSCILLOSCOPE.CH_SIZE
            for i in range(1, count+1):
                self._channels[i] = channels[i-1]
                pass
            print(self._channels, "CHANNELS")
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
            graph.plot(x,y, pen=color, name=y_name)
            graph.setLabel('bottom', "Time scale", units=str(x_Unit))
            graph.setLabel('left', "CH scale", units=str(y_Unit))
        else:
            console("Inequality", y_name, " ; ", sizex, " ; ", sizey)


    def clear_plotted_items(self, graph:pg.PlotWidget):
        dataItems = graph.listDataItems()
        for i in dataItems:
            # console(i.name(), " ", y_name)
            if i is not None:
                graph.removeItem(i)