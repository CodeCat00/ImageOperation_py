import numpy as np

from PySide6.QtWidgets import QLabel

from model.ImageOperationModel import ImageOperationModel
from control.convert.ImageConvert import cImageToQPixmap


# menu模板
def menuActionTemplate(func, model=ImageOperationModel, label=QLabel):
    # 深拷贝
    deepCopyImage = np.copy(model.getImageModel().inImage)
    # 处理
    image = func(deepCopyImage)
    # 更新界面
    updateImageInfo(image, model, label)


# 更新图像信息
def updateImageInfo(image, model=ImageOperationModel, label=QLabel):
    # 更新处理结果
    model.getImageModel().setDealImage(image)
    # 转换类型
    qPixmap = cImageToQPixmap(model.getImageModel().showImage)
    # 显示图片
    label.setPixmap(qPixmap)
