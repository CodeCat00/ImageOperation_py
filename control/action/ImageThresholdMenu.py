from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.ImageThresholdManager import simpleBinaryThreshold, simpleBinaryInvThreshold, simpleTruncThreshold, \
    simpleToZeroThreshold, simpleToZeroInvThreshold, adaptiveMeanThreshold, adaptiveGaussianThreshold, OTSUThreshold
from model.ImageOperationModel import ImageOperationModel


# 简单二值化阈值
def simpleBinaryThresholdAct(model=ImageOperationModel, label=QLabel):
    # 简单二值化阈值
    image = simpleBinaryThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 简单反二值化阈值
def simpleBinaryInvThresholdAct(model=ImageOperationModel, label=QLabel):
    # 简单反二值化阈值
    image = simpleBinaryInvThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 简单截断阈值
def simpleTruncThresholdAct(model=ImageOperationModel, label=QLabel):
    # 简单截断阈值
    image = simpleTruncThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 简单置零阈值
def simpleToZeroThresholdAct(model=ImageOperationModel, label=QLabel):
    # 简单置零阈值
    image = simpleToZeroThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 简单置零反阈值
def simpleToZeroInvThresholdAct(model=ImageOperationModel, label=QLabel):
    # 简单置零反阈值
    image = simpleToZeroInvThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 自适应均值阈值
def adaptiveMeanThresholdAct(model=ImageOperationModel, label=QLabel):
    # 自适应均值阈值
    image = adaptiveMeanThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 自适应高斯阈值
def adaptiveGaussianThresholdAct(model=ImageOperationModel, label=QLabel):
    # 自适应高斯阈值
    image = adaptiveGaussianThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# OTSU二值化
def OTSUThresholdAct(model=ImageOperationModel, label=QLabel):
    # 自适应高斯阈值
    image = OTSUThreshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
