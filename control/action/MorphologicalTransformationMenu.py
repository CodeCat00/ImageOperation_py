from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuDealTemplate
from control.image.MorphologicalTransformationManager import *
from model.ImageOperationModel import ImageOperationModel


# 腐蚀
def erosionAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(erosion, model, label)


# 膨胀
def dilateAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(dilate, model, label)


# 开运算
def morphologyExOpenAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(morphologyExOpen, model, label)


# 闭运算
def morphologyExCloseAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(morphologyExClose, model, label)


# 形态梯度
def morphologyExGradientAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(morphologyExGradient, model, label)


# 顶帽
def morphologyExTopHatAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(morphologyExTopHat, model, label)


# 黑帽
def morphologyExBlackHatAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(morphologyExBlackHat, model, label)
