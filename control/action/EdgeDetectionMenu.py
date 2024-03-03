from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.EdgeDetectionManager import canny
from model.ImageOperationModel import ImageOperationModel


# canny边缘检测
def cannyAct(model=ImageOperationModel, label=QLabel):
    # canny边缘检测
    image = canny(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
