import cv2

from control.image.ImageManager import resizeImage


class ImageModel:

    # 初始化
    def __init__(self, imageFile):
        self.initAttribute(imageFile)

    # 初始化属性
    def initAttribute(self, imageFile):
        self.inImage = cv2.imread(imageFile)
        self.showImage = resizeImage(self.inImage, 256, 2048, 1024)
