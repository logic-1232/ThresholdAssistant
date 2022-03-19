import cv2
import numpy as np
from PIL import Image


class MyImage(object):
    def getImage(self, imgPath) -> None:
        if(imgPath):
            # self.img = cv2.imread(imgPath)
            self.img = cv2.imdecode(np.fromfile(imgPath, dtype=np.uint8), -1)
            self.img = cv2.resize(self.img, (512, 512))
            self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.Qimg = Image.fromarray(self.img_rgb).toqpixmap()

    def operateImage(self, gamut, threshold):
        if(gamut == "LAB"):
            img_color = cv2.cvtColor(self.img, cv2.COLOR_BGR2LAB)
            lower = np.array(
                [threshold[0]*2.55, threshold[2]+128, threshold[4]+128])
            higher = np.array(
                [threshold[1]*2.55, threshold[3]+128, threshold[5]+128])
        elif(gamut == "HSV"):
            img_color = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
            lower = np.array([threshold[0], threshold[2], threshold[4]])
            higher = np.array([threshold[1], threshold[3], threshold[5]])
        elif(gamut == "RGB"):
            img_color = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            lower = np.array([threshold[0], threshold[2], threshold[4]])
            higher = np.array([threshold[1], threshold[3], threshold[5]])
        self.mask = cv2.inRange(img_color, lower, higher)
        # cv2.imshow("color", self.img)
        # cv2.imshow("self.mask", self.mask)
        # 转成pyqt中的图片
        self.Qmask = Image.fromarray(self.mask).toqpixmap()
