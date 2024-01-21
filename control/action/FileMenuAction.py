import cv2
from PySide6.QtWidgets import QFileDialog, QLabel, QStatusBar

from control.convert.ImageConvert import cImage2QPixmap
from control.file.FilePathManager import fetchFilePathModel
from model.ImageOperationModel import ImageOperationModel
from model.image.ImageModel import ImageModel


# 打开图片
def openAct(model=ImageOperationModel, label=QLabel):
    # 选择文件
    imageFile, _ = QFileDialog.getOpenFileNames(None, 'Open Images', '', 'Image files (*.png *.jpg *.jpeg)')
    # 读取图片
    imageModel = ImageModel(imageFile[0])
    # 显示图片
    label.setPixmap(cImage2QPixmap(imageModel.showImage))
    # 保存图像
    model.setImageModel(imageModel)


# 保存图片
def saveAct(model=ImageOperationModel, bar=QStatusBar):
    # 选择文件及路径
    imageFile, _ = QFileDialog.getSaveFileName(None, '设置保存路径', '', 'Image files (*.png *.jpg *.jpeg)')
    # 保存文件
    cv2.imwrite(imageFile, model.getImageModel().dealImage)
    # 显示状态栏
    bar.showMessage("保存路径：" + imageFile)


# 打开图片目录（自动显示第一张图片）
def openFilePathAct(model=ImageOperationModel, label=QLabel):
    # 获取图像文件列表
    imageFileModel = fetchFilePathModel()
    # 使用第一个图片地址
    imageFile = imageFileModel.getImageFile()
    # 读取图像
    imageModel = ImageModel(imageFile)
    # 显示图片
    label.setPixmap(cImage2QPixmap(imageModel.showImage))
    # 保存图像
    model.setImageModel(imageModel)
    # 保存图像文件模型
    model.setImageFileModel(imageFileModel)
