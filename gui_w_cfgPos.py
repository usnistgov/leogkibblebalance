# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_cfgPos.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 331, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.BTN_start = QtWidgets.QPushButton(self.groupBox_2)
        self.BTN_start.setGeometry(QtCore.QRect(10, 20, 151, 23))
        self.BTN_start.setObjectName("BTN_start")
        self.T_Instructions = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.T_Instructions.setGeometry(QtCore.QRect(10, 50, 311, 101))
        self.T_Instructions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_Instructions.setReadOnly(True)
        self.T_Instructions.setObjectName("T_Instructions")
        self.BTN_confirm = QtWidgets.QPushButton(self.groupBox_2)
        self.BTN_confirm.setEnabled(False)
        self.BTN_confirm.setGeometry(QtCore.QRect(190, 160, 131, 31))
        self.BTN_confirm.setObjectName("BTN_confirm")
        self.TXT_ready = QtWidgets.QLabel(self.groupBox_2)
        self.TXT_ready.setEnabled(False)
        self.TXT_ready.setGeometry(QtCore.QRect(110, 170, 61, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_ready.setPalette(palette)
        self.TXT_ready.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_ready.setObjectName("TXT_ready")
        self.TXT_wait = QtWidgets.QLabel(self.groupBox_2)
        self.TXT_wait.setEnabled(True)
        self.TXT_wait.setGeometry(QtCore.QRect(100, 150, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_wait.setPalette(palette)
        self.TXT_wait.setInputMethodHints(QtCore.Qt.ImhNone)
        self.TXT_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_wait.setObjectName("TXT_wait")
        self.TB_value = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.TB_value.setEnabled(False)
        self.TB_value.setGeometry(QtCore.QRect(10, 160, 81, 31))
        self.TB_value.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.TB_value.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TB_value.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.TB_value.setKeyboardTracking(False)
        self.TB_value.setDecimals(0)
        self.TB_value.setMinimum(0.0)
        self.TB_value.setMaximum(9999.0)
        self.TB_value.setProperty("value", 0.0)
        self.TB_value.setObjectName("TB_value")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 10, 321, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.T_points = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.T_points.setGeometry(QtCore.QRect(10, 20, 191, 121))
        self.T_points.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_points.setReadOnly(True)
        self.T_points.setObjectName("T_points")
        self.TB_degree = QtWidgets.QSpinBox(self.groupBox_3)
        self.TB_degree.setEnabled(False)
        self.TB_degree.setGeometry(QtCore.QRect(210, 30, 101, 31))
        self.TB_degree.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.TB_degree.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_degree.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TB_degree.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.TB_degree.setKeyboardTracking(False)
        self.TB_degree.setMinimum(-1)
        self.TB_degree.setMaximum(999999999)
        self.TB_degree.setProperty("value", -1)
        self.TB_degree.setObjectName("TB_degree")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.BTN_fit = QtWidgets.QPushButton(self.groupBox_3)
        self.BTN_fit.setEnabled(False)
        self.BTN_fit.setGeometry(QtCore.QRect(210, 70, 101, 31))
        self.BTN_fit.setObjectName("BTN_fit")
        self.BTN_savefit = QtWidgets.QPushButton(self.groupBox_3)
        self.BTN_savefit.setEnabled(False)
        self.BTN_savefit.setGeometry(QtCore.QRect(210, 110, 101, 31))
        self.BTN_savefit.setObjectName("BTN_savefit")
        self.T_fitresult = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.T_fitresult.setGeometry(QtCore.QRect(10, 150, 301, 41))
        self.T_fitresult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_fitresult.setReadOnly(True)
        self.T_fitresult.setObjectName("T_fitresult")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 661, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.PW_fits = PlotWidget(self.groupBox_4)
        self.PW_fits.setGeometry(QtCore.QRect(10, 40, 641, 171))
        self.PW_fits.setObjectName("PW_fits")
        self.TXT_calculatedfit = QtWidgets.QLabel(self.groupBox_4)
        self.TXT_calculatedfit.setGeometry(QtCore.QRect(10, 20, 81, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_calculatedfit.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_calculatedfit.setFont(font)
        self.TXT_calculatedfit.setObjectName("TXT_calculatedfit")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.TXT_currentfit = QtWidgets.QLabel(self.groupBox_4)
        self.TXT_currentfit.setGeometry(QtCore.QRect(170, 20, 331, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_currentfit.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_currentfit.setFont(font)
        self.TXT_currentfit.setObjectName("TXT_currentfit")
        self.TXT_currentfit_2 = QtWidgets.QLabel(self.groupBox_4)
        self.TXT_currentfit_2.setGeometry(QtCore.QRect(510, 20, 151, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_currentfit_2.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_currentfit_2.setFont(font)
        self.TXT_currentfit_2.setObjectName("TXT_currentfit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calibrate Position"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Take Sample Points:"))
        self.BTN_start.setText(_translate("MainWindow", "Start Calibration"))
        self.T_Instructions.setPlainText(_translate("MainWindow", "Start the Calibration, \n"
"then follow the Instructions here!"))
        self.BTN_confirm.setText(_translate("MainWindow", "Confirm"))
        self.TXT_ready.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">READY</span></p></body></html>"))
        self.TXT_wait.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">WAIT</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Fitting Points:"))
        self.T_points.setPlainText(_translate("MainWindow", "Once you took samplepoints, they will be displayed here:\n"
"\n"
""))
        self.label_2.setText(_translate("MainWindow", "Degree of PolyFit:"))
        self.BTN_fit.setText(_translate("MainWindow", "Fit"))
        self.BTN_savefit.setText(_translate("MainWindow", "Save fit "))
        self.T_fitresult.setPlainText(_translate("MainWindow", "Once you fitted your points, the Fit will be shown here:\n"
"(highest Polynomial first)\n"
"\n"
""))
        self.groupBox_4.setTitle(_translate("MainWindow", "Fit:"))
        self.TXT_calculatedfit.setText(_translate("MainWindow", "Calculated Fit"))
        self.label_5.setText(_translate("MainWindow", "Current Fit:"))
        self.TXT_currentfit.setText(_translate("MainWindow", "I AM JUST CLEANING HERE"))
        self.TXT_currentfit_2.setText(_translate("MainWindow", "(highest polynomial first)"))
from pyqtgraph import PlotWidget
