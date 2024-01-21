import os

from PySide6.QtWidgets import QFileDialog

from model.file.ImageFileModel import ImageFileModel


# 获取图片地址
def fetchFilePathModel():
    # 变量
    imageFiles = []
    # 用户选择文件
    filePath = QFileDialog.getExistingDirectory(None, '选择文件夹')
    if filePath is None:
        return
    # 筛选出所有图片文件路径集合
    for file in os.listdir(filePath):
        if file.endswith('.jpg') or file.endswith('.png'):
            imageFiles.append(filePath + "/" + file)
    # 创建并返回对象
    return ImageFileModel(imageFiles)
