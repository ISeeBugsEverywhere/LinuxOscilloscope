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
        oscillWindow.resize(1078, 976)
        self.centralwidget = QtWidgets.QWidget(oscillWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout_2.addWidget(self.quitButton, 3, 0, 1, 1)
        self.info_lbl = QtWidgets.QLabel(self.centralwidget)
        self.info_lbl.setObjectName("info_lbl")
        self.gridLayout_2.addWidget(self.info_lbl, 4, 0, 1, 1)
        self.dir_label = QtWidgets.QLabel(self.centralwidget)
        self.dir_label.setObjectName("dir_label")
        self.gridLayout_2.addWidget(self.dir_label, 4, 1, 1, 2)
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
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
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
        self.autoConnect = QtWidgets.QPushButton(self.centralwidget)
        self.autoConnect.setIconSize(QtCore.QSize(32, 32))
        self.autoConnect.setObjectName("autoConnect")
        self.horizontalLayout.addWidget(self.autoConnect)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setIconSize(QtCore.QSize(32, 32))
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.rescan_ports_button = QtWidgets.QPushButton(self.centralwidget)
        self.rescan_ports_button.setIconSize(QtCore.QSize(32, 32))
        self.rescan_ports_button.setObjectName("rescan_ports_button")
        self.horizontalLayout.addWidget(self.rescan_ports_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(765, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.oscilloscopeTab = QtWidgets.QWidget()
        self.oscilloscopeTab.setObjectName("oscilloscopeTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.oscilloscopeTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.live_update_box = QtWidgets.QCheckBox(self.groupBox_2)
        self.live_update_box.setObjectName("live_update_box")
        self.gridLayout_5.addWidget(self.live_update_box, 1, 0, 1, 1)
        self.sleep_time_box = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sleep_time_box.setMinimum(0.01)
        self.sleep_time_box.setProperty("value", 1.0)
        self.sleep_time_box.setObjectName("sleep_time_box")
        self.gridLayout_5.addWidget(self.sleep_time_box, 1, 1, 1, 1)
        self.corZeroBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.corZeroBox.setObjectName("corZeroBox")
        self.gridLayout_5.addWidget(self.corZeroBox, 2, 0, 1, 2)
        self.get_data_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.get_data_btn.setEnabled(False)
        self.get_data_btn.setMaximumSize(QtCore.QSize(220, 16777215))
        self.get_data_btn.setObjectName("get_data_btn")
        self.gridLayout_5.addWidget(self.get_data_btn, 0, 0, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ch3_comment = QtWidgets.QLineEdit(self.groupBox)
        self.ch3_comment.setEnabled(False)
        self.ch3_comment.setObjectName("ch3_comment")
        self.gridLayout_4.addWidget(self.ch3_comment, 6, 1, 1, 2)
        self.ch1_comment = QtWidgets.QLineEdit(self.groupBox)
        self.ch1_comment.setEnabled(False)
        self.ch1_comment.setObjectName("ch1_comment")
        self.gridLayout_4.addWidget(self.ch1_comment, 4, 1, 1, 2)
        self.ch2_comment = QtWidgets.QLineEdit(self.groupBox)
        self.ch2_comment.setEnabled(False)
        self.ch2_comment.setObjectName("ch2_comment")
        self.gridLayout_4.addWidget(self.ch2_comment, 5, 1, 1, 2)
        self.file_name_entry = QtWidgets.QLineEdit(self.groupBox)
        self.file_name_entry.setObjectName("file_name_entry")
        self.gridLayout_4.addWidget(self.file_name_entry, 0, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 6, 0, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.groupBox)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout_4.addWidget(self.save_btn, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 7, 0, 1, 1)
        self.ch4_comment = QtWidgets.QLineEdit(self.groupBox)
        self.ch4_comment.setEnabled(False)
        self.ch4_comment.setObjectName("ch4_comment")
        self.gridLayout_4.addWidget(self.ch4_comment, 7, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 5, 0, 1, 1)
        self.dir_btn = QtWidgets.QPushButton(self.groupBox)
        self.dir_btn.setObjectName("dir_btn")
        self.gridLayout_4.addWidget(self.dir_btn, 1, 2, 1, 1)
        self.saved_state_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saved_state_label.setFont(font)
        self.saved_state_label.setObjectName("saved_state_label")
        self.gridLayout_4.addWidget(self.saved_state_label, 2, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 8, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 4, 0, 1, 2)
        self.channel_group_box = QtWidgets.QGroupBox(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channel_group_box.sizePolicy().hasHeightForWidth())
        self.channel_group_box.setSizePolicy(sizePolicy)
        self.channel_group_box.setMaximumSize(QtCore.QSize(220, 16777215))
        self.channel_group_box.setObjectName("channel_group_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.channel_group_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ch1_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch1_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ch1_btn.setCheckable(True)
        self.ch1_btn.setChecked(False)
        self.ch1_btn.setObjectName("ch1_btn")
        self.gridLayout_3.addWidget(self.ch1_btn, 0, 0, 1, 1)
        self.ch2_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch2_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ch2_btn.setCheckable(True)
        self.ch2_btn.setObjectName("ch2_btn")
        self.gridLayout_3.addWidget(self.ch2_btn, 0, 1, 1, 1)
        self.ch3_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch3_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ch3_btn.setCheckable(True)
        self.ch3_btn.setObjectName("ch3_btn")
        self.gridLayout_3.addWidget(self.ch3_btn, 1, 0, 1, 1)
        self.ch4_btn = QtWidgets.QPushButton(self.channel_group_box)
        self.ch4_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ch4_btn.setCheckable(True)
        self.ch4_btn.setObjectName("ch4_btn")
        self.gridLayout_3.addWidget(self.ch4_btn, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.channel_group_box, 1, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 0, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem7, 0, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 6, 1, 1, 1)
        self.saveAllBtn = QtWidgets.QPushButton(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAllBtn.sizePolicy().hasHeightForWidth())
        self.saveAllBtn.setSizePolicy(sizePolicy)
        self.saveAllBtn.setObjectName("saveAllBtn")
        self.gridLayout_7.addWidget(self.saveAllBtn, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem9, 7, 1, 1, 1)
        self.clrButton = QtWidgets.QPushButton(self.oscilloscopeTab)
        self.clrButton.setObjectName("clrButton")
        self.gridLayout_7.addWidget(self.clrButton, 4, 1, 1, 1)
        self.oscillographPlot = PlotWidget(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oscillographPlot.sizePolicy().hasHeightForWidth())
        self.oscillographPlot.setSizePolicy(sizePolicy)
        self.oscillographPlot.setMinimumSize(QtCore.QSize(600, 450))
        self.oscillographPlot.setObjectName("oscillographPlot")
        self.gridLayout_7.addWidget(self.oscillographPlot, 0, 0, 7, 1)
        self.formulaEdit = QtWidgets.QLineEdit(self.oscilloscopeTab)
        self.formulaEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.formulaEdit.setObjectName("formulaEdit")
        self.gridLayout_7.addWidget(self.formulaEdit, 7, 0, 1, 1)
        self.minusMButton = QtWidgets.QPushButton(self.oscilloscopeTab)
        self.minusMButton.setObjectName("minusMButton")
        self.gridLayout_7.addWidget(self.minusMButton, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 1, 1, 1, 1)
        self.plusMButton = QtWidgets.QPushButton(self.oscilloscopeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusMButton.sizePolicy().hasHeightForWidth())
        self.plusMButton.setSizePolicy(sizePolicy)
        self.plusMButton.setObjectName("plusMButton")
        self.gridLayout_7.addWidget(self.plusMButton, 2, 1, 1, 1)
        self.logMode = QtWidgets.QPushButton(self.oscilloscopeTab)
        self.logMode.setObjectName("logMode")
        self.gridLayout_7.addWidget(self.logMode, 5, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 2, 1, 1)
        self.tabWidget.addTab(self.oscilloscopeTab, "")
        self.parametersTab = QtWidgets.QWidget()
        self.parametersTab.setObjectName("parametersTab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.parametersTab)
        self.gridLayout_10.setObjectName("gridLayout_10")
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
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem11, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_4, 0, 2, 1, 1)
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
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem12, 3, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 0, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem13, 0, 4, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.parametersTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.idnButton = QtWidgets.QPushButton(self.groupBox_3)
        self.idnButton.setObjectName("idnButton")
        self.gridLayout.addWidget(self.idnButton, 0, 0, 1, 1)
        self.rstButton = QtWidgets.QPushButton(self.groupBox_3)
        self.rstButton.setObjectName("rstButton")
        self.gridLayout.addWidget(self.rstButton, 0, 1, 1, 1)
        self.unlockButton = QtWidgets.QPushButton(self.groupBox_3)
        self.unlockButton.setObjectName("unlockButton")
        self.gridLayout.addWidget(self.unlockButton, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(419, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 0, 3, 1, 1)
        self.cmdsButton = QtWidgets.QPushButton(self.groupBox_3)
        self.cmdsButton.setObjectName("cmdsButton")
        self.gridLayout.addWidget(self.cmdsButton, 0, 4, 1, 1)
        self.executeAllButton = QtWidgets.QPushButton(self.groupBox_3)
        self.executeAllButton.setObjectName("executeAllButton")
        self.gridLayout.addWidget(self.executeAllButton, 0, 5, 1, 1)
        self.cmdsBox = QtWidgets.QComboBox(self.groupBox_3)
        self.cmdsBox.setEditable(True)
        self.cmdsBox.setObjectName("cmdsBox")
        self.gridLayout.addWidget(self.cmdsBox, 1, 0, 1, 5)
        self.executeButton = QtWidgets.QPushButton(self.groupBox_3)
        self.executeButton.setObjectName("executeButton")
        self.gridLayout.addWidget(self.executeButton, 1, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 149, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 2, 5, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.groupBox_3)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 3, 5, 1, 1)
        self.outputBox = QtWidgets.QTextEdit(self.groupBox_3)
        self.outputBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.outputBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.outputBox.setObjectName("outputBox")
        self.gridLayout.addWidget(self.outputBox, 2, 0, 2, 5)
        self.gridLayout_10.addWidget(self.groupBox_3, 2, 0, 1, 5)
        self.rs232Widget = serialPortWidget(self.parametersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rs232Widget.sizePolicy().hasHeightForWidth())
        self.rs232Widget.setSizePolicy(sizePolicy)
        self.rs232Widget.setMinimumSize(QtCore.QSize(120, 30))
        self.rs232Widget.setObjectName("rs232Widget")
        self.gridLayout_10.addWidget(self.rs232Widget, 0, 0, 1, 2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.parametersTab)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 140))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.name_all_box = QtWidgets.QLineEdit(self.groupBox_7)
        self.name_all_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name_all_box.setObjectName("name_all_box")
        self.gridLayout_12.addWidget(self.name_all_box, 0, 0, 1, 5)
        self.memory_box = QtWidgets.QComboBox(self.groupBox_7)
        self.memory_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.memory_box.setObjectName("memory_box")
        self.memory_box.addItem("")
        self.memory_box.addItem("")
        self.memory_box.addItem("")
        self.memory_box.addItem("")
        self.gridLayout_12.addWidget(self.memory_box, 0, 5, 1, 1)
        self.help_button = QtWidgets.QPushButton(self.groupBox_7)
        self.help_button.setMinimumSize(QtCore.QSize(31, 31))
        self.help_button.setMaximumSize(QtCore.QSize(32, 32))
        self.help_button.setObjectName("help_button")
        self.gridLayout_12.addWidget(self.help_button, 0, 6, 1, 1)
        self.take_screenshot_btn = QtWidgets.QPushButton(self.groupBox_7)
        self.take_screenshot_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.take_screenshot_btn.setObjectName("take_screenshot_btn")
        self.gridLayout_12.addWidget(self.take_screenshot_btn, 1, 0, 2, 1)
        spacerItem16 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem16, 1, 1, 2, 1)
        self.save_csv_button = QtWidgets.QPushButton(self.groupBox_7)
        self.save_csv_button.setObjectName("save_csv_button")
        self.gridLayout_12.addWidget(self.save_csv_button, 1, 2, 2, 1)
        spacerItem17 = QtWidgets.QSpacerItem(124, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem17, 1, 3, 2, 1)
        self.save_all_button = QtWidgets.QPushButton(self.groupBox_7)
        self.save_all_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.save_all_button.setObjectName("save_all_button")
        self.gridLayout_12.addWidget(self.save_all_button, 1, 4, 2, 1)
        spacerItem18 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem18, 2, 5, 1, 2)
        self.gridLayout_10.addWidget(self.groupBox_7, 1, 0, 1, 3)
        self.tabWidget.addTab(self.parametersTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.infoTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.clear_btn = QtWidgets.QPushButton(self.infoTab)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout_8.addWidget(self.clear_btn, 0, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(857, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem19, 0, 1, 1, 1)
        self.infoText = QtWidgets.QTextEdit(self.infoTab)
        self.infoText.setObjectName("infoText")
        self.gridLayout_8.addWidget(self.infoText, 1, 0, 1, 2)
        self.tabWidget.addTab(self.infoTab, "")
        self.helpPageTab = QtWidgets.QWidget()
        self.helpPageTab.setObjectName("helpPageTab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.helpPageTab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.webWidget = QtWebEngineWidgets.QWebEngineView(self.helpPageTab)
        self.webWidget.setObjectName("webWidget")
        self.gridLayout_15.addWidget(self.webWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.helpPageTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 3)
        oscillWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(oscillWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 27))
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
        self.quitButton.setText(_translate("oscillWindow", "Quit"))
        self.info_lbl.setText(_translate("oscillWindow", "File will be saved in:"))
        self.dir_label.setText(_translate("oscillWindow", "Directory?"))
        self.label.setText(_translate("oscillWindow", "Oscilloscope:"))
        self.idnLabel.setText(_translate("oscillWindow", "<html><head/><body><p><span style=\" font-weight:600;\">If it is connected, IDN will be shown here.</span></p></body></html>"))
        self.lxiRadio.setText(_translate("oscillWindow", "L&XI?"))
        self.rs232Radio.setText(_translate("oscillWindow", "RS&232?"))
        self.usbtmcRadio.setText(_translate("oscillWindow", "&USBTMC?"))
        self.autoConnect.setText(_translate("oscillWindow", "AUTO[..]"))
        self.connectButton.setText(_translate("oscillWindow", "Connect"))
        self.rescan_ports_button.setText(_translate("oscillWindow", "Rescan ports"))
        self.groupBox_2.setTitle(_translate("oscillWindow", "Observation"))
        self.live_update_box.setText(_translate("oscillWindow", "Live update,\n"
"every [s]:"))
        self.corZeroBox.setText(_translate("oscillWindow", "Correct Zero Level?"))
        self.get_data_btn.setText(_translate("oscillWindow", "Get data from\n"
"active channel(s)"))
        self.groupBox.setTitle(_translate("oscillWindow", "Save Box"))
        self.file_name_entry.setPlaceholderText(_translate("oscillWindow", "File name?"))
        self.label_8.setText(_translate("oscillWindow", "CH3 comm."))
        self.save_btn.setText(_translate("oscillWindow", "Save"))
        self.label_9.setText(_translate("oscillWindow", "CH4 comm."))
        self.label_2.setText(_translate("oscillWindow", "CH1 comm."))
        self.label_3.setText(_translate("oscillWindow", "CH2 comm."))
        self.dir_btn.setText(_translate("oscillWindow", "Directory?"))
        self.saved_state_label.setText(_translate("oscillWindow", "(UNSAVED)"))
        self.channel_group_box.setTitle(_translate("oscillWindow", "Active channel"))
        self.ch1_btn.setText(_translate("oscillWindow", "CH1"))
        self.ch2_btn.setText(_translate("oscillWindow", "CH2"))
        self.ch3_btn.setText(_translate("oscillWindow", "CH3"))
        self.ch4_btn.setText(_translate("oscillWindow", "CH4"))
        self.saveAllBtn.setText(_translate("oscillWindow", "Save All"))
        self.clrButton.setText(_translate("oscillWindow", "CLR"))
        self.formulaEdit.setPlaceholderText(_translate("oscillWindow", "vars: y, np.sqrt(), /,*,-,+"))
        self.minusMButton.setText(_translate("oscillWindow", "-M"))
        self.plusMButton.setText(_translate("oscillWindow", "+M"))
        self.logMode.setText(_translate("oscillWindow", "LOG(X,Y)"))
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
        self.groupBox_3.setTitle(_translate("oscillWindow", "SCPI commands"))
        self.idnButton.setText(_translate("oscillWindow", "IDN?"))
        self.rstButton.setText(_translate("oscillWindow", "RST"))
        self.unlockButton.setText(_translate("oscillWindow", "UNLOCK"))
        self.cmdsButton.setText(_translate("oscillWindow", "Commands ..."))
        self.executeAllButton.setText(_translate("oscillWindow", "Execute all"))
        self.executeButton.setText(_translate("oscillWindow", "Execute"))
        self.clearButton.setText(_translate("oscillWindow", "Clear"))
        self.groupBox_7.setTitle(_translate("oscillWindow", "Screenshots/Internal Memory"))
        self.name_all_box.setPlaceholderText(_translate("oscillWindow", "name of a file?"))
        self.memory_box.setItemText(0, _translate("oscillWindow", "E:"))
        self.memory_box.setItemText(1, _translate("oscillWindow", "F:"))
        self.memory_box.setItemText(2, _translate("oscillWindow", "G:"))
        self.memory_box.setItemText(3, _translate("oscillWindow", "H:"))
        self.help_button.setText(_translate("oscillWindow", "?"))
        self.take_screenshot_btn.setText(_translate("oscillWindow", "Screenshot?"))
        self.save_csv_button.setText(_translate("oscillWindow", "Save *.CSV"))
        self.save_all_button.setText(_translate("oscillWindow", "Save all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parametersTab), _translate("oscillWindow", "Parameters"))
        self.clear_btn.setText(_translate("oscillWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), _translate("oscillWindow", "Output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.helpPageTab), _translate("oscillWindow", "HELP"))
        self.menuFile.setTitle(_translate("oscillWindow", "Fi&le"))
        self.actionQuit_Ctrl_Q.setText(_translate("oscillWindow", "&Quit(Ctrl+Q)"))
from PyQt5 import QtWebEngineWidgets
from GUI.serialPortWidget.serialPortWidget import serialPortWidget
from pyqtgraph import PlotWidget
