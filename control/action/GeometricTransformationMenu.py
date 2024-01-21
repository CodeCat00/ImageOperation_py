from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.GeometricTransformationManager import resize, translation, rotation, warpAffine, warpPerspective
from model.ImageOperationModel import ImageOperationModel


# 缩放操作
def resizeAct(model=ImageOperationModel, label=QLabel):
    # 缩放处理
    image = resize(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 平移操作
def translationAct(model=ImageOperationModel, label=QLabel):
    # 平移处理
    image = translation(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 旋转操作
def rotationAct(model=ImageOperationModel, label=QLabel):
    # 旋转处理
    image = rotation(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 仿射变换操作
def warpAffineAct(model=ImageOperationModel, label=QLabel):
    # 仿射变换处理
    image = warpAffine(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 透视变换操作
def warpPerspectiveAct(model=ImageOperationModel, label=QLabel):
    # 透视变换处理
    image = warpPerspective(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
