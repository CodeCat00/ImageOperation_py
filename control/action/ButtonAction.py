from PySide6.QtWidgets import QLabel

from control.convert.ImageConvert import cImage2QPixmap
from model.ImageOperationmodel import ImageOperationModel
from model.image.ImageModel import ImageModel


def preImage(model=ImageOperationModel, label=QLabel):
    # 获取前一张图片地址
    imageFile = model.getImageFileModel().getPreImageFile()
    # 读取图像
    imageModel = ImageModel(imageFile)
    # 显示图片
    label.setPixmap(cImage2QPixmap(imageModel.showImage))
    # 保存图片
    model.setImageModel(imageModel)


def nextImage(model=ImageOperationModel, label=QLabel):
    # 获取前一张图片地址
    imageFile = model.getImageFileModel().getNextImageFile()
    # 读取图像
    imageModel = ImageModel(imageFile)
    # 显示图片
    label.setPixmap(cImage2QPixmap(imageModel.showImage))
    # 保存图片
    model.setImageModel(imageModel)
