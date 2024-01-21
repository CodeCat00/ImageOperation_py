import cv2

from control.image.ImageBasicManager import resizeImage


class ImageModel:

    # 初始化
    def __init__(self, imageFile):
        self.initAttribute(imageFile)

    # 初始化属性
    def initAttribute(self, imageFile):
        self.inImage = cv2.imread(imageFile)
        self.dealImage = self.inImage
        self.showImage = resizeImage(self.dealImage, 256, 2048, 1024)

    # 更新图像处理图片
    def setDealImage(self, image):
        self.dealImage = image
        self.showImage = resizeImage(self.dealImage, 256, 2048, 1024)
