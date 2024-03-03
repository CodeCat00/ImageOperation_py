from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.ContourManager import *
from model.ImageOperationModel import ImageOperationModel


# 轮廓近似
def approxPolyDPAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(approxPolyDP, model, label)


# 凸包
def convexHullAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(convexHull, model, label)


# 旋转矩形
def drawContoursAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(drawContours, model, label)


# 最小外圆
def circleAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(circle, model, label)


# 拟合椭圆
def ellipseAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(ellipse, model, label)


# 拟合线
def lineAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(line, model, label)
