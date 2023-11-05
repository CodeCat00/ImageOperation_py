from PySide6.QtWidgets import QLabel

from control.convert.ImageConvert import cImage2QPixmap
from control.image.ImageManager import threshold
from model.ImageOperationmodel import ImageOperationModel


def thresholdAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = threshold(model.getImageModel().inImage)
    # 更新处理结果
    model.getImageModel().setDealImage(image)
    # 显示图片
    label.setPixmap(cImage2QPixmap(model.getImageModel().showImage))