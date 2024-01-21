from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication

from control.action.ButtonAction import preImage, nextImage
from control.action.ColorAdjustmentAction import grayProcessingAct, imageInversionAct
from control.action.FileMenuAction import openAct, saveAct, openFilePathAct
from model.ImageOperationModel import ImageOperationModel
from view.ui.Ui_MainUi import Ui_MainUi


class Window(QMainWindow):

    # 初始化
    def __init__(self):
        # super
        super().__init__()
        # 初始化属性
        self.initAttribute()
        # 从文件中加载界面
        self.loadUi()
        # 关联槽函数
        self.fileMenuConnect()
        self.buttonConnect()
        self.colorAdjustmentMenuConnect()

    # 初始化属性
    def initAttribute(self):
        self.model = ImageOperationModel()

    # 加载界面
    def loadUi(self):
        self.ui = Ui_MainUi()
        self.ui.setupUi(self)

    # 连接文件菜单处理方法
    def fileMenuConnect(self):
        self.ui.actionOpen.triggered.connect(partial(openAct, self.model, self.ui.openImageFileLabel))
        self.ui.actionSave.triggered.connect(partial(saveAct, self.model, self.ui.statusBar))
        self.ui.actionOpenFilePath.triggered.connect(partial(openFilePathAct, self.model, self.ui.openImageFileLabel))
        self.ui.actionExit.triggered.connect(QApplication.instance().quit)

    # 连接切换图像按钮方法
    def buttonConnect(self):
        self.ui.preImageButton.clicked.connect((partial(preImage, self.model, self.ui.openImageFileLabel)))
        self.ui.nextImageButton.clicked.connect((partial(nextImage, self.model, self.ui.openImageFileLabel)))

    # 色彩调整
    def colorAdjustmentMenuConnect(self):
        self.ui.actionGrayProcessing.triggered.connect((partial(grayProcessingAct, self.model, self.ui.tabLabel1)))
        self.ui.actionImageInversion.triggered.connect((partial(imageInversionAct, self.model, self.ui.tabLabel1)))

    # 图像滤波器
    def imageBlurMenuConnect(self):
        pass

    # 图像噪声
    def noiseMenuConnect(self):
        pass

    # 形态学
    def morphologyMenuConnect(self):
        pass

    # 图像分割
    def imageSegmentationMenuConnect(self):
        pass
