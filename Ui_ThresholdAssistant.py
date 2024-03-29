# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\86158\OneDrive\VSCodeProject\project_py\pyqt\ThresholdAssistant\ThresholdAssistant.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1055, 788)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gamut_label = QtWidgets.QLabel(self.centralwidget)
        self.gamut_label.setObjectName("gamut_label")
        self.horizontalLayout.addWidget(self.gamut_label)
        self.gamut_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.gamut_comboBox.setMinimumSize(QtCore.QSize(64, 0))
        self.gamut_comboBox.setObjectName("gamut_comboBox")
        self.gamut_comboBox.addItem("")
        self.gamut_comboBox.addItem("")
        self.gamut_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.gamut_comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.getImage_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getImage_pushButton.setObjectName("getImage_pushButton")
        self.horizontalLayout.addWidget(self.getImage_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.first_low_label = QtWidgets.QLabel(self.centralwidget)
        self.first_low_label.setObjectName("first_low_label")
        self.gridLayout.addWidget(self.first_low_label, 0, 0, 1, 1)
        self.first_low_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.first_low_horizontalSlider.setMaximum(100)
        self.first_low_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.first_low_horizontalSlider.setInvertedAppearance(False)
        self.first_low_horizontalSlider.setInvertedControls(False)
        self.first_low_horizontalSlider.setObjectName("first_low_horizontalSlider")
        self.gridLayout.addWidget(self.first_low_horizontalSlider, 0, 1, 1, 1)
        self.first_low_result_label = QtWidgets.QLabel(self.centralwidget)
        self.first_low_result_label.setMinimumSize(QtCore.QSize(36, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_low_result_label.setFont(font)
        self.first_low_result_label.setObjectName("first_low_result_label")
        self.gridLayout.addWidget(self.first_low_result_label, 0, 2, 1, 1)
        self.first_high_label = QtWidgets.QLabel(self.centralwidget)
        self.first_high_label.setObjectName("first_high_label")
        self.gridLayout.addWidget(self.first_high_label, 1, 0, 1, 1)
        self.first_high_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.first_high_horizontalSlider.setMinimum(0)
        self.first_high_horizontalSlider.setMaximum(100)
        self.first_high_horizontalSlider.setProperty("value", 100)
        self.first_high_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.first_high_horizontalSlider.setInvertedAppearance(False)
        self.first_high_horizontalSlider.setInvertedControls(False)
        self.first_high_horizontalSlider.setObjectName("first_high_horizontalSlider")
        self.gridLayout.addWidget(self.first_high_horizontalSlider, 1, 1, 1, 1)
        self.first_high_result_label = QtWidgets.QLabel(self.centralwidget)
        self.first_high_result_label.setMinimumSize(QtCore.QSize(36, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_high_result_label.setFont(font)
        self.first_high_result_label.setObjectName("first_high_result_label")
        self.gridLayout.addWidget(self.first_high_result_label, 1, 2, 1, 1)
        self.second_low_label = QtWidgets.QLabel(self.centralwidget)
        self.second_low_label.setObjectName("second_low_label")
        self.gridLayout.addWidget(self.second_low_label, 2, 0, 1, 1)
        self.second_low_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.second_low_horizontalSlider.setMinimum(-128)
        self.second_low_horizontalSlider.setMaximum(127)
        self.second_low_horizontalSlider.setProperty("value", -128)
        self.second_low_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.second_low_horizontalSlider.setObjectName("second_low_horizontalSlider")
        self.gridLayout.addWidget(self.second_low_horizontalSlider, 2, 1, 1, 1)
        self.second_low_result_label = QtWidgets.QLabel(self.centralwidget)
        self.second_low_result_label.setMinimumSize(QtCore.QSize(36, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.second_low_result_label.setFont(font)
        self.second_low_result_label.setObjectName("second_low_result_label")
        self.gridLayout.addWidget(self.second_low_result_label, 2, 2, 1, 1)
        self.second_high_label = QtWidgets.QLabel(self.centralwidget)
        self.second_high_label.setObjectName("second_high_label")
        self.gridLayout.addWidget(self.second_high_label, 3, 0, 1, 1)
        self.second_high_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.second_high_horizontalSlider.setMinimum(-128)
        self.second_high_horizontalSlider.setMaximum(127)
        self.second_high_horizontalSlider.setProperty("value", 127)
        self.second_high_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.second_high_horizontalSlider.setInvertedAppearance(False)
        self.second_high_horizontalSlider.setObjectName("second_high_horizontalSlider")
        self.gridLayout.addWidget(self.second_high_horizontalSlider, 3, 1, 1, 1)
        self.second_high_result_label = QtWidgets.QLabel(self.centralwidget)
        self.second_high_result_label.setMinimumSize(QtCore.QSize(36, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.second_high_result_label.setFont(font)
        self.second_high_result_label.setObjectName("second_high_result_label")
        self.gridLayout.addWidget(self.second_high_result_label, 3, 2, 1, 1)
        self.third_low_label = QtWidgets.QLabel(self.centralwidget)
        self.third_low_label.setObjectName("third_low_label")
        self.gridLayout.addWidget(self.third_low_label, 4, 0, 1, 1)
        self.third_low_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.third_low_horizontalSlider.setMinimum(-128)
        self.third_low_horizontalSlider.setMaximum(127)
        self.third_low_horizontalSlider.setProperty("value", -128)
        self.third_low_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.third_low_horizontalSlider.setObjectName("third_low_horizontalSlider")
        self.gridLayout.addWidget(self.third_low_horizontalSlider, 4, 1, 1, 1)
        self.third_low_result_label = QtWidgets.QLabel(self.centralwidget)
        self.third_low_result_label.setMinimumSize(QtCore.QSize(36, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.third_low_result_label.setFont(font)
        self.third_low_result_label.setObjectName("third_low_result_label")
        self.gridLayout.addWidget(self.third_low_result_label, 4, 2, 1, 1)
        self.third_high_label = QtWidgets.QLabel(self.centralwidget)
        self.third_high_label.setObjectName("third_high_label")
        self.gridLayout.addWidget(self.third_high_label, 5, 0, 1, 1)
        self.third_high_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.third_high_horizontalSlider.setMinimum(-128)
        self.third_high_horizontalSlider.setMaximum(127)
        self.third_high_horizontalSlider.setProperty("value", 127)
        self.third_high_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.third_high_horizontalSlider.setInvertedAppearance(False)
        self.third_high_horizontalSlider.setObjectName("third_high_horizontalSlider")
        self.gridLayout.addWidget(self.third_high_horizontalSlider, 5, 1, 1, 1)
        self.third_high_result_label = QtWidgets.QLabel(self.centralwidget)
        self.third_high_result_label.setMinimumSize(QtCore.QSize(36, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.third_high_result_label.setFont(font)
        self.third_high_result_label.setObjectName("third_high_result_label")
        self.gridLayout.addWidget(self.third_high_result_label, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.threshold_label = QtWidgets.QLabel(self.centralwidget)
        self.threshold_label.setObjectName("threshold_label")
        self.horizontalLayout_2.addWidget(self.threshold_label)
        self.threshold_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.threshold_lineEdit.setEnabled(False)
        self.threshold_lineEdit.setObjectName("threshold_lineEdit")
        self.horizontalLayout_2.addWidget(self.threshold_lineEdit)
        self.copy_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.copy_pushButton.setObjectName("copy_pushButton")
        self.horizontalLayout_2.addWidget(self.copy_pushButton)
        self.reset_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_pushButton.setSizePolicy(sizePolicy)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout_2.addWidget(self.reset_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setMinimumSize(QtCore.QSize(512, 512))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout_3.addWidget(self.image_label)
        self.mask_label = QtWidgets.QLabel(self.centralwidget)
        self.mask_label.setMinimumSize(QtCore.QSize(512, 512))
        self.mask_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_label.setObjectName("mask_label")
        self.horizontalLayout_3.addWidget(self.mask_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Threshold Assistant"))
        self.gamut_label.setText(_translate("MainWindow", "选择色域："))
        self.gamut_comboBox.setItemText(0, _translate("MainWindow", "LAB"))
        self.gamut_comboBox.setItemText(1, _translate("MainWindow", "HSV"))
        self.gamut_comboBox.setItemText(2, _translate("MainWindow", "RGB"))
        self.getImage_pushButton.setText(_translate("MainWindow", "选择图片"))
        self.first_low_label.setText(_translate("MainWindow", "L最小值"))
        self.first_low_result_label.setText(_translate("MainWindow", "0"))
        self.first_high_label.setText(_translate("MainWindow", "L最大值"))
        self.first_high_result_label.setText(_translate("MainWindow", "100"))
        self.second_low_label.setText(_translate("MainWindow", "A最小值"))
        self.second_low_result_label.setText(_translate("MainWindow", "-128"))
        self.second_high_label.setText(_translate("MainWindow", "A最大值"))
        self.second_high_result_label.setText(_translate("MainWindow", "127"))
        self.third_low_label.setText(_translate("MainWindow", "B最小值"))
        self.third_low_result_label.setText(_translate("MainWindow", "-128"))
        self.third_high_label.setText(_translate("MainWindow", "B最大值"))
        self.third_high_result_label.setText(_translate("MainWindow", "127"))
        self.threshold_label.setText(_translate("MainWindow", "LAB阈值"))
        self.copy_pushButton.setText(_translate("MainWindow", "复制阈值"))
        self.reset_pushButton.setText(_translate("MainWindow", "重置"))
        self.image_label.setText(_translate("MainWindow", "彩色原图"))
        self.mask_label.setText(_translate("MainWindow", "二值化图片"))
