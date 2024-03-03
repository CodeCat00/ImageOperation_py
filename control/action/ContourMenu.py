from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuDealTemplate
from control.image.ContourManager import *
from model.ImageOperationModel import ImageOperationModel


# 轮廓近似
def approxPolyDPAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(approxPolyDP, model, label)


# 凸包
def convexHullAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(convexHull, model, label)


# 旋转矩形
def drawContoursAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(drawContours, model, label)


# 最小外圆
def circleAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(circle, model, label)


# 拟合椭圆
def ellipseAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(ellipse, model, label)


# 拟合线
def lineAct(model=ImageOperationModel, label=QLabel):
    menuDealTemplate(line, model, label)
