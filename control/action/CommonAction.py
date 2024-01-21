# 更新图像信息
from PySide6.QtWidgets import QLabel

from control.convert.ImageConvert import cImage2QPixmap
from model.ImageOperationModel import ImageOperationModel


# 更新图像信息
def updateImageInfo(image, model=ImageOperationModel, label=QLabel):
    # 更新处理结果
    model.getImageModel().setDealImage(image)
    # 显示图片
    label.setPixmap(cImage2QPixmap(model.getImageModel().showImage))