import os
import sys

import pyperclip
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from MyImage import MyImage
from Ui_ThresholdAssistant import Ui_MainWindow


class MyThresholdAssistant(QtWidgets.QMainWindow, Ui_MainWindow, MyImage):
    def __init__(self):
        super(MyThresholdAssistant, self).__init__()
        self.setupUi(self)
        self.LAB = [0, 100, -128, 127, -128, 127]
        self.HSV = [0, 180, 0, 255, 0, 255]
        self.RGB = [0, 255, 0, 255, 0, 255]
        self.connect()  # 连接控件和槽函数
        self.changeGamut()  # 获取色彩空间，并初始化设置
        self.loadImage()  # 加载图片并显示

    def connect(self):
        """连接控件与槽函数"""
        self.getImage_pushButton.clicked.connect(self.loadImage)
        self.gamut_comboBox.currentIndexChanged.connect(self.changeGamut)
        self.first_low_horizontalSlider.valueChanged.connect(
            self.changeThreshold_0)
        self.first_high_horizontalSlider.valueChanged.connect(
            self.changeThreshold_1)
        self.second_low_horizontalSlider.valueChanged.connect(
            self.changeThreshold_2)
        self.second_high_horizontalSlider.valueChanged.connect(
            self.changeThreshold_3)
        self.third_low_horizontalSlider.valueChanged.connect(
            self.changeThreshold_4)
        self.third_high_horizontalSlider.valueChanged.connect(
            self.changeThreshold_5)
        self.reset_pushButton.clicked.connect(self.resetThreshold)
        self.copy_pushButton.clicked.connect(self.copyTreshold)

    def loadImage(self):
        """加载图片并显示"""
        self.imgPath, fileType = QFileDialog.getOpenFileName(
            self, "选择图片", os.getcwd(), "*.jpg *.jpeg *.png")
        self.getImage(self.imgPath)
        self.showImage()

    def changeGamut(self):
        """修改颜色空间并重置阈值"""
        self.gamut = self.gamut_comboBox.currentText()
        self.first_low_label.setText(self.gamut[0]+"最小值")
        self.first_high_label.setText(self.gamut[0]+"最大值")
        self.second_low_label.setText(self.gamut[1]+"最小值")
        self.second_high_label.setText(self.gamut[1]+"最大值")
        self.third_low_label.setText(self.gamut[2]+"最小值")
        self.third_high_label.setText(self.gamut[2]+"最大值")
        self.threshold_label.setText(self.gamut+"阈值")
        self.resetThreshold()

    def resetThreshold(self):
        """重置阈值"""
        if(self.gamut == "LAB"):
            self.threshold = self.LAB.copy()
        elif(self.gamut == "HSV"):
            self.threshold = self.HSV.copy()
        elif(self.gamut == "RGB"):
            self.threshold = self.RGB.copy()
        # 阈值取值范围
        self.first_low_horizontalSlider.setMinimum(self.threshold[0])
        self.first_low_horizontalSlider.setMaximum(self.threshold[1])
        self.first_high_horizontalSlider.setMinimum(self.threshold[0])
        self.first_high_horizontalSlider.setMaximum(self.threshold[1])
        self.second_low_horizontalSlider.setMinimum(self.threshold[2])
        self.second_low_horizontalSlider.setMaximum(self.threshold[3])
        self.second_high_horizontalSlider.setMinimum(self.threshold[2])
        self.second_high_horizontalSlider.setMaximum(self.threshold[3])
        self.third_low_horizontalSlider.setMinimum(self.threshold[4])
        self.third_low_horizontalSlider.setMaximum(self.threshold[5])
        self.third_high_horizontalSlider.setMinimum(self.threshold[4])
        self.third_high_horizontalSlider.setMaximum(self.threshold[5])
        # 设置阈值为最大范围
        self.first_low_horizontalSlider.setValue(self.threshold[0])
        self.first_high_horizontalSlider.setValue(self.threshold[1])
        self.second_low_horizontalSlider.setValue(self.threshold[2])
        self.second_high_horizontalSlider.setValue(self.threshold[3])
        self.third_low_horizontalSlider.setValue(self.threshold[4])
        self.third_high_horizontalSlider.setValue(self.threshold[5])
        self.threshold_lineEdit.setText(str(self.threshold))

    def showImage(self):
        """显示图片"""
        if(self.imgPath):
            self.operateImage(self.gamut, self.threshold)
            self.image_label.setPixmap(self.Qimg)
            self.mask_label.setPixmap(self.Qmask)

    def changeThreshold_0(self):
        self.threshold[0] = self.first_low_horizontalSlider.value()
        self.first_low_result_label.setText(str(self.threshold[0]))
        self.threshold_lineEdit.setText(str(self.threshold))
        self.showImage()

    def changeThreshold_1(self):
        self.threshold[1] = self.first_high_horizontalSlider.value()
        self.first_high_result_label.setText(str(self.threshold[1]))
        self.threshold_lineEdit.setText(str(self.threshold))
        self.showImage()

    def changeThreshold_2(self):
        self.threshold[2] = self.second_low_horizontalSlider.value()
        self.second_low_result_label.setText(str(self.threshold[2]))
        self.threshold_lineEdit.setText(str(self.threshold))
        self.showImage()

    def changeThreshold_3(self):
        self.threshold[3] = self.second_high_horizontalSlider.value()
        self.second_high_result_label.setText(str(self.threshold[3]))
        self.threshold_lineEdit.setText(str(self.threshold))
        self.showImage()

    def changeThreshold_4(self):
        self.threshold[4] = self.third_low_horizontalSlider.value()
        self.third_low_result_label.setText(str(self.threshold[4]))
        self.threshold_lineEdit.setText(str(self.threshold))
        self.showImage()

    def changeThreshold_5(self):
        self.threshold[5] = self.third_high_horizontalSlider.value()
        self.third_high_result_label.setText(str(self.threshold[5]))
        self.threshold_lineEdit.setText(str(self.threshold))
        self.showImage()

    def copyTreshold(self):
        """复制阈值到剪贴板"""
        pyperclip.copy(str(self.threshold))
        QMessageBox.information(self, "提示", "阈值复制成功！")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyThresholdAssistant()
    myshow.show()
    sys.exit(app.exec_())
