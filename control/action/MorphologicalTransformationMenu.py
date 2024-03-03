from PySide6.QtWidgets import QLabel

from control.action.CommonAction import updateImageInfo
from control.image.MorphologicalTransformationManager import erosion, dilate, morphologyExOpen, morphologyExClose, \
    morphologyExGradient, morphologyExTopHat, morphologyExBlackHat
from model.ImageOperationModel import ImageOperationModel


# 腐蚀
def erosionAct(model=ImageOperationModel, label=QLabel):
    # 腐蚀
    image = erosion(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 膨胀
def dilateAct(model=ImageOperationModel, label=QLabel):
    # 膨胀
    image = dilate(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 开运算
def morphologyExOpenAct(model=ImageOperationModel, label=QLabel):
    # 开运算
    image = morphologyExOpen(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 闭运算
def morphologyExCloseAct(model=ImageOperationModel, label=QLabel):
    # 闭运算
    image = morphologyExClose(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 形态梯度
def morphologyExGradientAct(model=ImageOperationModel, label=QLabel):
    # 形态梯度
    image = morphologyExGradient(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 顶帽
def morphologyExTopHatAct(model=ImageOperationModel, label=QLabel):
    # 顶帽
    image = morphologyExTopHat(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


# 黑帽
def morphologyExBlackHatAct(model=ImageOperationModel, label=QLabel):
    # 黑帽
    image = morphologyExBlackHat(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
