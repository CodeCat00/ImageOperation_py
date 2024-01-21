from PySide6.QtWidgets import QLabel

from control.convert.ImageConvert import cImageToQPixmap
from model.ImageOperationModel import ImageOperationModel
from model.image.ImageModel import ImageModel


# 切换前一张图片
def preImage(model=ImageOperationModel, label=QLabel):
    # 获取前一张图片地址
    imageFile = model.getImageFileModel().getPreImageFile()
    # 读取图像
    imageModel = ImageModel(imageFile)
    # 显示图片
    label.setPixmap(cImageToQPixmap(imageModel.showImage))
    # 保存图片
    model.setImageModel(imageModel)


# 切换后一张图片
def nextImage(model=ImageOperationModel, label=QLabel):
    # 获取前一张图片地址
    imageFile = model.getImageFileModel().getNextImageFile()
    # 读取图像
    imageModel = ImageModel(imageFile)
    # 显示图片
    label.setPixmap(cImageToQPixmap(imageModel.showImage))
    # 保存图片
    model.setImageModel(imageModel)
