from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.GeometricTransformationManager import *
from model.ImageOperationModel import ImageOperationModel


# 缩放操作
def resizeAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(resize, model, label)


# 平移操作
def translationAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(translation, model, label)


# 旋转操作
def rotationAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(rotation, model, label)


# 仿射变换操作
def warpAffineAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(warpAffine, model, label)


# 透视变换操作
def warpPerspectiveAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(warpPerspective, model, label)
