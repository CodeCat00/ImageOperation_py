from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.ImageThresholdManager import *
from model.ImageOperationModel import ImageOperationModel


# 简单二值化阈值
def simpleBinaryThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(simpleBinaryThreshold, model, label)


# 简单反二值化阈值
def simpleBinaryInvThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(simpleBinaryInvThreshold, model, label)


# 简单截断阈值
def simpleTruncThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(simpleTruncThreshold, model, label)


# 简单置零阈值
def simpleToZeroThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(simpleToZeroThreshold, model, label)


# 简单置零反阈值
def simpleToZeroInvThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(simpleToZeroInvThreshold, model, label)


# 自适应均值阈值
def adaptiveMeanThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(adaptiveMeanThreshold, model, label)


# 自适应高斯阈值
def adaptiveGaussianThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(adaptiveGaussianThreshold, model, label)


# OTSU二值化
def OTSUThresholdAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(OTSUThreshold, model, label)
