#!/usr/bin/python3
#-*- utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui, QtSerialPort
from PyQt5.QtCore import QIODevice, pyqtSlot, pyqtSignal
# from serialPlotWidget.serialPortWidgetForm import Ui_serialPortWidget
import serial
from GUI.serialPortWidget.serialPortWidgetForm import Ui_serialPortWidget


class serialPortWidget(QtWidgets.QWidget):
        returnPorts = pyqtSignal(list)
        _parity_serial = (
                serial.PARITY_NONE,
                serial.PARITY_EVEN,
                serial.PARITY_MARK,
                serial.PARITY_ODD,
                serial.PARITY_SPACE
        )

        BAUDRATES = (
                QtSerialPort.QSerialPort().Baud1200,
                QtSerialPort.QSerialPort().Baud2400,
                QtSerialPort.QSerialPort().Baud4800,
                QtSerialPort.QSerialPort().Baud9600,
                QtSerialPort.QSerialPort().Baud19200,
                QtSerialPort.QSerialPort().Baud38400,
                QtSerialPort.QSerialPort().Baud57600,
                QtSerialPort.QSerialPort().Baud115200,
        )

        DATABITS = (
                QtSerialPort.QSerialPort().Data5,
                QtSerialPort.QSerialPort().Data6,
                QtSerialPort.QSerialPort().Data7,
                QtSerialPort.QSerialPort().Data8,
        )

        FLOWCONTROL = (
                QtSerialPort.QSerialPort().NoFlowControl,
                QtSerialPort.QSerialPort().HardwareControl,
                QtSerialPort.QSerialPort().SoftwareControl,
        )

        PARITY = (
                QtSerialPort.QSerialPort().NoParity,
                QtSerialPort.QSerialPort().EvenParity,
                QtSerialPort.QSerialPort().OddParity,
                QtSerialPort.QSerialPort().SpaceParity,
                QtSerialPort.QSerialPort().MarkParity,
        )

        STOPBITS = (
                QtSerialPort.QSerialPort().OneStop,
                QtSerialPort.QSerialPort().TwoStop,
                QtSerialPort.QSerialPort().OneAndHalfStop,

        )
        def __init__(self, parent=None):
                super(serialPortWidget, self).__init__()
                self.ui = Ui_serialPortWidget()
                self.ui.setupUi(self)
                self.fillSerialPortFields()
                self.serialPort = QtSerialPort.QSerialPort()
                self.UpdateLabels()
                self.ui.parityBox.currentIndexChanged.connect(self.UpdateLabels)
                self.ui.stopBitsBox.currentIndexChanged.connect(self.UpdateLabels)
                # self.ui.comPortBox.currentIndexChanged.connect()
                pass

        def UpdateLabels(self):
                dict_parity={
                        QtSerialPort.QSerialPort().NoParity:"No Parity",
                        QtSerialPort.QSerialPort().EvenParity:"Even Parity",
                        QtSerialPort.QSerialPort().OddParity:"Odd Parity",
                        QtSerialPort.QSerialPort().SpaceParity:"Space Parity",
                        QtSerialPort.QSerialPort().MarkParity:"MarkParity"
                }
                dict_stopBits={
                        QtSerialPort.QSerialPort().OneStop:"One Stop",
                        QtSerialPort.QSerialPort().TwoStop:"Two Stop",
                        QtSerialPort.QSerialPort().OneAndHalfStop:"1,5 Stop",
                }
                label = dict_parity[int(self.ui.parityBox.currentText())]
                self.ui.parityInformation.setText(label)
                label = dict_stopBits[int(self.ui.stopBitsBox.currentText())]
                self.ui.StopBitsInformation.setText(label)
                pass

        def getSerialPort(self):
                self.serialPort.setPortName(self.ui.comPortBox.currentText())
                self.serialPort.setDataBits(self.DATABITS[self.ui.dataBitsBox.currentIndex()])
                self.serialPort.setBaudRate(self.BAUDRATES[self.ui.baudRateBox.currentIndex()])
                self.serialPort.setStopBits(self.STOPBITS[self.ui.stopBitsBox.currentIndex()])
                self.serialPort.setParity(self.PARITY[self.ui.parityBox.currentIndex()])
                return self.serialPort
                pass

        def fillSerialPortFields(self):
                self.ui.baudRateBox.insertItems(0, [str(x) for x in self.BAUDRATES])
                self.ui.dataBitsBox.insertItems(0, [str(x) for x in self.DATABITS])
                self.ui.stopBitsBox.insertItems(0, [str(x) for x in self.STOPBITS])
                self.ui.parityBox.insertItems(0, [str(x) for x in self.PARITY])
                ports = QtSerialPort.QSerialPortInfo().availablePorts()
                self.ui.comPortBox.insertItems(0, [str(x.portName()) for x in ports])
                baud_rate_index = self.ui.baudRateBox.findText("9600")
                self.ui.baudRateBox.setCurrentIndex(baud_rate_index)
                data_bits_index = self.ui.dataBitsBox.findText("8")
                self.ui.dataBitsBox.setCurrentIndex(data_bits_index)
                pass

        @pyqtSlot()
        def rescan_ports(self):
                self.ui.comPortBox.clear()
                ports = QtSerialPort.QSerialPortInfo().availablePorts()
                self.ui.comPortBox.insertItems(0, [str(x.portName()) for x in ports])
                self.returnPorts.emit(ports)
                pass

        def get_port_names(self):
                ports = QtSerialPort.QSerialPortInfo().availablePorts()
                return ports
                pass

        def update_ports_in_box(self, index):
                if index >= 0:
                        self.ui.comPortBox.setCurrentIndex(index)
                pass

        def return_serial_dict(self):
                """
                Returns a dictionary filled with parameters, suitable for pySerial
                :return:
                """
                params = {}
                params['baudrate'] = int(self.ui.baudRateBox.currentText())
                params['bytesize'] = int(self.ui.dataBitsBox.currentText())
                p = self.ui.parityBox.currentText()

                return params
                pass