from PySide6.QtWidgets import QFileDialog, QLabel

from control.convert.ImageConvert import cImage2QPixmap
from control.image.ImageManager import threshold
from model.ImageOperationmodel import ImageOperationModel
from model.image.ImageModel import ImageModel


def openAct(model=ImageOperationModel, label=QLabel):
    # 选择文件
    imageFile, _ = QFileDialog.getOpenFileNames(None, 'Open Images', '../', 'Image files (*.png *.jpg *.jpeg)')
    # 读取图片
    imageModel = ImageModel(imageFile[0])
    # 显示图片
    label.setPixmap(cImage2QPixmap(imageModel.showImage))
    # 保存图像
    model.setImageModel(imageModel)


def thresholdAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = threshold(model.getImageModel().showImage)
    # 显示图片
    label.setPixmap(cImage2QPixmap(image))
