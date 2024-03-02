from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.ImageSmoothManager import filter2D, blur, gaussianBlur, medianBlur, bilateralFilter
from model.ImageOperationModel import ImageOperationModel


# 二维卷积
def filter2DAct(model=ImageOperationModel, label=QLabel):
    # 二维卷积
    image = filter2D(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 均值模糊
def blurAct(model=ImageOperationModel, label=QLabel):
    # 均值模糊
    image = blur(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 高斯模糊
def gaussianBlurAct(model=ImageOperationModel, label=QLabel):
    # 高斯模糊
    image = gaussianBlur(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 中值滤波
def medianBlurAct(model=ImageOperationModel, label=QLabel):
    # 中值滤波
    image = medianBlur(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 双边滤波
def bilateralFilterAct(model=ImageOperationModel, label=QLabel):
    # 双边滤波
    image = bilateralFilter(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
