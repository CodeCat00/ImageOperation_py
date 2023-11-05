from model.file.ImageFileModel import ImageFileModel
from model.image.ImageModel import ImageModel


class ImageOperationModel:

    def __init__(self):
        self.imageModel = ImageModel
        self.imageFileModel = ImageFileModel

    def getImageModel(self):
        return self.imageModel

    def setImageModel(self, model):
        self.imageModel = model

    def getImageFileModel(self):
        return self.imageFileModel

    def setImageFileModel(self, imageFileModel):
        self.imageFileModel = imageFileModel
