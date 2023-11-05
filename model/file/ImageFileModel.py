class ImageFileModel:

    # 初始化
    def __init__(self, imageFiles):
        self.initAttribute(imageFiles)

    # 初始化属性
    def initAttribute(self, imageFiles):
        self.index = 0
        self.imageFiles = imageFiles

    # 获取图片文件地址
    def getImageFile(self):
        return self.index

    # 获取前一张图片地址
    def getNextImageFile(self):
        return self.getDiffPosPreImageFile(1)

    # 获取后一张图片地址
    def getPreImageFile(self):
        return self.getDiffPosPreImageFile(-1)

    # 获取指定位置图片地址
    def getDiffPosPreImageFile(self, diffPos):
        size = self.imageFiles.size()
        self.index = (self.index + size + diffPos) / size
        return self.index
