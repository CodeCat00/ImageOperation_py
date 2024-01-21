from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.ColorAdjustmentManager import gray, flip
from model.ImageOperationModel import ImageOperationModel


# 灰度操作
def grayProcessingAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = gray(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 反转操作
def imageInversionAct(model=ImageOperationModel, label=QLabel):
    # 反转处理
    image = flip(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
