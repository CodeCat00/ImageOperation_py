import cv2

from control.image.ImageManager import resizeImage


class ImageModel:

    # 初始化
    def __init__(self, imageFile):
        self.initAttribute(imageFile)

    # 初始化属性
    def initAttribute(self, imageFile):
        self.inImage = cv2.imread(imageFile)
        self.dealImage = self.inImage
        self.showImage = resizeImage(self.dealImage, 256, 2048, 1024)

    def setDealImage(self, image):
        self.dealImage = image
        self.showImage = resizeImage(self.dealImage, 256, 2048, 1024)
