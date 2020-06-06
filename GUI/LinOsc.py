# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LinOsc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_oscillWindow(object):
    def setupUi(self, oscillWindow):
        oscillWindow.setObjectName("oscillWindow")
        oscillWindow.resize(989, 717)
        self.centralwidget = QtWidgets.QWidget(oscillWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.idnLabel = QtWidgets.QLabel(self.centralwidget)
        self.idnLabel.setTextFormat(QtCore.Qt.RichText)
        self.idnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idnLabel.setObjectName("idnLabel")
        self.horizontalLayout_2.addWidget(self.idnLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lxiRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.lxiRadio.setChecked(True)
        self.lxiRadio.setObjectName("lxiRadio")
        self.horizontalLayout.addWidget(self.lxiRadio)
        self.lxiCombo = QtWidgets.QComboBox(self.centralwidget)
        self.lxiCombo.setMinimumSize(QtCore.QSize(200, 30))
        self.lxiCombo.setEditable(True)
        self.lxiCombo.setObjectName("lxiCombo")
        self.horizontalLayout.addWidget(self.lxiCombo)
        self.rs232Radio = QtWidgets.QRadioButton(self.centralwidget)
        self.rs232Radio.setObjectName("rs232Radio")
        self.horizontalLayout.addWidget(self.rs232Radio)
        self.rs232Combo = QtWidgets.QComboBox(self.centralwidget)
        self.rs232Combo.setEnabled(False)
        self.rs232Combo.setObjectName("rs232Combo")
        self.horizontalLayout.addWidget(self.rs232Combo)
        self.usbtmcRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.usbtmcRadio.setObjectName("usbtmcRadio")
        self.horizontalLayout.addWidget(self.usbtmcRadio)
        self.usbtmcCombo = QtWidgets.QComboBox(self.centralwidget)
        self.usbtmcCombo.setEnabled(False)
        self.usbtmcCombo.setObjectName("usbtmcCombo")
        self.horizontalLayout.addWidget(self.usbtmcCombo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout_2.addWidget(self.quitButton, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(765, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.oscilloscopeTab = QtWidgets.QWidget()
        self.oscilloscopeTab.setObjectName("oscilloscopeTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.oscilloscopeTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.get_data_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.get_data_btn.setObjectName("get_data_btn")
        self.gridLayout_5.addWidget(self.get_data_btn, 0, 0, 1, 3)
        self.same_curve_box = QtWidgets.QCheckBox(self.groupBox_2)
        self.same_curve_box.setChecked(True)
        self.same_curve_box.setObjectName("same_curve_box")
        self.gridLayout_5.addWidget(self.same_curve_box, 1, 0, 1, 3)
        self.live_update_box = QtWidgets.QCheckBox(self.groupBox_2)
        self.live_update_box.setObjectName("live_update_box")
        self.gridLayout_5.addWidget(self.live_update_box, 2, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 3, 0, 1, 1)
        self.channel_open_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.channel_open_btn.setObjectName("channel_open_btn")
        self.gridLayout_5.addWidget(self.channel_open_btn, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 3, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.file_name_entry = QtWidgets.QLineEdit(self.groupBox)
        self.file_name_entry.setObjectName("file_name_entry")
        self.gridLayout_4.addWidget(self.file_name_entry, 0, 0, 1, 3)
        self.save_btn = QtWidgets.QPushButton(self.groupBox)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout_4.addWidget(self.save_btn, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 1, 1, 1, 1)
        self.dir_btn = QtWidgets.QPushButton(self.groupBox)
        self.dir_btn.setObjectName("dir_btn")
        self.gridLayout_4.addWidget(self.dir_btn, 1, 2, 1, 1)
        self.dir_label = QtWidgets.QLabel(self.groupBox)
        self.dir_label.setObjectName("dir_label")
        self.gridLayout_4.addWidget(self.dir_label, 2, 0, 1, 3)
        self.gridLayout_6.addWidget(self.groupBox, 4, 0, 1, 2)
        self.channel_group_box = QtWidgets.QGroupBox(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channel_group_box.sizePolicy().hasHeightForWidth())
        self.channel_group_box.setSizePolicy(sizePolicy)
        self.channel_group_box.setObjectName("channel_group_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.channel_group_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ch1_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch1_btn.setCheckable(True)
        self.ch1_btn.setChecked(False)
        self.ch1_btn.setObjectName("ch1_btn")
        self.gridLayout_3.addWidget(self.ch1_btn, 0, 0, 1, 1)
        self.ch2_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch2_btn.setCheckable(True)
        self.ch2_btn.setObjectName("ch2_btn")
        self.gridLayout_3.addWidget(self.ch2_btn, 0, 1, 1, 1)
        self.ch3_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch3_btn.setCheckable(True)
        self.ch3_btn.setObjectName("ch3_btn")
        self.gridLayout_3.addWidget(self.ch3_btn, 1, 0, 1, 1)
        self.ch4_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch4_btn.setCheckable(True)
        self.ch4_btn.setObjectName("ch4_btn")
        self.gridLayout_3.addWidget(self.ch4_btn, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.channel_group_box, 1, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem8, 0, 1, 1, 1)
        self.oscillographPlot = PlotWidget(self.oscilloscopeTab)
        self.oscillographPlot.setObjectName("oscillographPlot")
        self.gridLayout_7.addWidget(self.oscillographPlot, 0, 2, 2, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.oscilloscopeTab, "")
        self.parametersTab = QtWidgets.QWidget()
        self.parametersTab.setObjectName("parametersTab")
        self.gridLayout = QtWidgets.QGridLayout(self.parametersTab)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem10 = QtWidgets.QSpacerItem(20, 238, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 3, 1, 1)
        self.rs232Widget = serialPortWidget(self.parametersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rs232Widget.sizePolicy().hasHeightForWidth())
        self.rs232Widget.setSizePolicy(sizePolicy)
        self.rs232Widget.setMinimumSize(QtCore.QSize(0, 30))
        self.rs232Widget.setObjectName("rs232Widget")
        self.gridLayout.addWidget(self.rs232Widget, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.parametersTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)
        self.usbtmc_encoding_box = QtWidgets.QComboBox(self.groupBox_4)
        self.usbtmc_encoding_box.setObjectName("usbtmc_encoding_box")
        self.usbtmc_encoding_box.addItem("")
        self.usbtmc_encoding_box.addItem("")
        self.gridLayout_13.addWidget(self.usbtmc_encoding_box, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_13.addWidget(self.label_5, 1, 0, 1, 1)
        self.usbtmc_errors_box = QtWidgets.QComboBox(self.groupBox_4)
        self.usbtmc_errors_box.setObjectName("usbtmc_errors_box")
        self.usbtmc_errors_box.addItem("")
        self.usbtmc_errors_box.addItem("")
        self.gridLayout_13.addWidget(self.usbtmc_errors_box, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem12, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.parametersTab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.selay_btw_commands = QtWidgets.QSpinBox(self.groupBox_5)
        self.selay_btw_commands.setObjectName("selay_btw_commands")
        self.gridLayout_14.addWidget(self.selay_btw_commands, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_14.addWidget(self.label_7, 1, 0, 1, 2)
        self.variable_edit_box = QtWidgets.QLineEdit(self.groupBox_5)
        self.variable_edit_box.setObjectName("variable_edit_box")
        self.gridLayout_14.addWidget(self.variable_edit_box, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem13, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)
        self.tabWidget.addTab(self.parametersTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.infoTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.clear_btn = QtWidgets.QPushButton(self.infoTab)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout_8.addWidget(self.clear_btn, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(857, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem14, 0, 1, 1, 1)
        self.infoText = QtWidgets.QTextEdit(self.infoTab)
        self.infoText.setObjectName("infoText")
        self.gridLayout_8.addWidget(self.infoText, 1, 0, 1, 2)
        self.tabWidget.addTab(self.infoTab, "")
        self.screeshotTab = QtWidgets.QWidget()
        self.screeshotTab.setObjectName("screeshotTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.screeshotTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.take_screenshot_btn = QtWidgets.QPushButton(self.screeshotTab)
        self.take_screenshot_btn.setObjectName("take_screenshot_btn")
        self.gridLayout_9.addWidget(self.take_screenshot_btn, 0, 0, 1, 1)
        self.save_screenshot_btn = QtWidgets.QPushButton(self.screeshotTab)
        self.save_screenshot_btn.setObjectName("save_screenshot_btn")
        self.gridLayout_9.addWidget(self.save_screenshot_btn, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(754, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem15, 0, 2, 1, 1)
        self.screenshotView = QtWidgets.QGraphicsView(self.screeshotTab)
        self.screenshotView.setObjectName("screenshotView")
        self.gridLayout_9.addWidget(self.screenshotView, 1, 0, 1, 3)
        self.tabWidget.addTab(self.screeshotTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        oscillWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(oscillWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        oscillWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(oscillWindow)
        self.statusbar.setObjectName("statusbar")
        oscillWindow.setStatusBar(self.statusbar)
        self.actionQuit_Ctrl_Q = QtWidgets.QAction(oscillWindow)
        self.actionQuit_Ctrl_Q.setObjectName("actionQuit_Ctrl_Q")
        self.menuFile.addAction(self.actionQuit_Ctrl_Q)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(oscillWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(oscillWindow)

    def retranslateUi(self, oscillWindow):
        _translate = QtCore.QCoreApplication.translate
        oscillWindow.setWindowTitle(_translate("oscillWindow", "Oscilloscope"))
        self.label.setText(_translate("oscillWindow", "Oscilloscope:"))
        self.idnLabel.setText(_translate("oscillWindow", "<html><head/><body><p><span style=\" font-weight:600;\">If it is connected, IDN will be shown here.</span></p></body></html>"))
        self.lxiRadio.setText(_translate("oscillWindow", "L&XI?"))
        self.rs232Radio.setText(_translate("oscillWindow", "RS&232?"))
        self.usbtmcRadio.setText(_translate("oscillWindow", "&USBTMC?"))
        self.connectButton.setText(_translate("oscillWindow", "Connect"))
        self.quitButton.setText(_translate("oscillWindow", "Quit"))
        self.groupBox_2.setTitle(_translate("oscillWindow", "Observation"))
        self.get_data_btn.setText(_translate("oscillWindow", "Get data from active channel"))
        self.same_curve_box.setText(_translate("oscillWindow", "Use the same curve?"))
        self.live_update_box.setText(_translate("oscillWindow", "Live update (On the same curve)"))
        self.channel_open_btn.setText(_translate("oscillWindow", "Channel On/Off"))
        self.groupBox.setTitle(_translate("oscillWindow", "Save Box"))
        self.file_name_entry.setPlaceholderText(_translate("oscillWindow", "File name?"))
        self.save_btn.setText(_translate("oscillWindow", "Save"))
        self.dir_btn.setText(_translate("oscillWindow", "Directory?"))
        self.dir_label.setText(_translate("oscillWindow", "Directory?"))
        self.channel_group_box.setTitle(_translate("oscillWindow", "Active channel"))
        self.ch1_btn.setText(_translate("oscillWindow", "CH1"))
        self.ch2_btn.setText(_translate("oscillWindow", "CH2"))
        self.ch3_btn.setText(_translate("oscillWindow", "CH3"))
        self.ch4_btn.setText(_translate("oscillWindow", "CH4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.oscilloscopeTab), _translate("oscillWindow", "Oscilloscope"))
        self.groupBox_4.setTitle(_translate("oscillWindow", "USBTMC options"))
        self.label_4.setText(_translate("oscillWindow", "Encoding"))
        self.usbtmc_encoding_box.setItemText(0, _translate("oscillWindow", "utf-8"))
        self.usbtmc_encoding_box.setItemText(1, _translate("oscillWindow", "ascii"))
        self.label_5.setText(_translate("oscillWindow", "Errors handling"))
        self.usbtmc_errors_box.setItemText(0, _translate("oscillWindow", "ignore"))
        self.usbtmc_errors_box.setItemText(1, _translate("oscillWindow", "replace"))
        self.groupBox_5.setTitle(_translate("oscillWindow", "Parameters for SCPI scripts"))
        self.label_6.setText(_translate("oscillWindow", "Variable in scripts"))
        self.label_7.setText(_translate("oscillWindow", "Delay between commands"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parametersTab), _translate("oscillWindow", "Parameters"))
        self.clear_btn.setText(_translate("oscillWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), _translate("oscillWindow", "Output"))
        self.take_screenshot_btn.setText(_translate("oscillWindow", "Screenshot?"))
        self.save_screenshot_btn.setText(_translate("oscillWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.screeshotTab), _translate("oscillWindow", "Screenshot"))
        self.menuFile.setTitle(_translate("oscillWindow", "Fi&le"))
        self.actionQuit_Ctrl_Q.setText(_translate("oscillWindow", "&Quit(Ctrl+Q)"))
from GUI.serialPortWidget.serialPortWidget import serialPortWidget
from pyqtgraph import PlotWidget
