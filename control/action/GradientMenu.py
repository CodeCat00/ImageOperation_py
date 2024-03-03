from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.GradientManager import laplacian, sobelX, sobelY
from model.ImageOperationModel import ImageOperationModel


# Laplacian微分
def laplacianAct(model=ImageOperationModel, label=QLabel):
    # Laplacian微分
    image = laplacian(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# sobelX
def sobelXAct(model=ImageOperationModel, label=QLabel):
    # sobelX
    image = sobelX(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# sobelY
def sobelYAct(model=ImageOperationModel, label=QLabel):
    # sobelY
    image = sobelY(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
