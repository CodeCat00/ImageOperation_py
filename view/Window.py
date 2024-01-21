from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication

from control.action.ButtonAction import preImage, nextImage
from control.action.ColorAdjustmentAction import grayProcessingAct
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
        self.opencvMenuConnect()
        self.buttonConnect()

    # 初始化属性
    def initAttribute(self):
        self.model = ImageOperationModel()

    # 加载界面
    def loadUi(self):
        self.ui = Ui_MainUi()
        self.ui.setupUi(self)

    # 连接文件菜单处理方法
    def fileMenuConnect(self):
        self.ui.openAct.triggered.connect(partial(openAct, self.model, self.ui.openImageFileLabel))
        self.ui.saveAct.triggered.connect(partial(saveAct, self.model, self.ui.statusBar))
        self.ui.openFilePathAct.triggered.connect(partial(openFilePathAct, self.model, self.ui.openImageFileLabel))
        self.ui.exitAct.triggered.connect(QApplication.instance().quit)

    # 连接切换图像按钮方法
    def buttonConnect(self):
        self.ui.preImageButton.clicked.connect((partial(preImage, self.model, self.ui.openImageFileLabel)))
        self.ui.nextImageButton.clicked.connect((partial(nextImage, self.model, self.ui.openImageFileLabel)))

    def opencvMenuConnect(self):
        self.ui.blurAct.triggered.connect((partial(grayProcessingAct, self.model, self.ui.tabLabel1)))
