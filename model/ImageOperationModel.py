from model.file.ImageFileModel import ImageFileModel
from model.image.ImageModel import ImageModel


class ImageOperationModel:

    # 初始化
    def __init__(self):
        self.imageModel = ImageModel
        self.imageFileModel = ImageFileModel

    # 获取图片模型
    def getImageModel(self):
        return self.imageModel

    # 更新图片模型
    def setImageModel(self, model):
        self.imageModel = model

    # 获取图片文件模型
    def getImageFileModel(self):
        return self.imageFileModel

    # 更新图片文件模型
    def setImageFileModel(self, imageFileModel):
        self.imageFileModel = imageFileModel
