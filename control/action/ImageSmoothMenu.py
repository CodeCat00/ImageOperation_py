from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.ImageSmoothManager import *
from model.ImageOperationModel import ImageOperationModel


# 二维卷积
def filter2DAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(filter2D, model, label)


# 均值模糊
def blurAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(blur, model, label)


# 高斯模糊
def gaussianBlurAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(gaussianBlur, model, label)


# 中值滤波
def medianBlurAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(medianBlur, model, label)


# 双边滤波
def bilateralFilterAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(bilateralFilter, model, label)
