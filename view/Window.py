from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication

from control.action.ButtonAction import preImage, nextImage
from control.action.FileMenuAction import openAct, saveAct, openFilePathAct
from control.action.OpenCVAction import thresholdAct
from model.ImageOperationmodel import ImageOperationModel
from view.ui.Ui_MainUi import Ui_MainUi


class Window(QMainWindow):

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

    def initAttribute(self):
        self.model = ImageOperationModel()

    def loadUi(self):
        self.ui = Ui_MainUi()
        self.ui.setupUi(self)

    def fileMenuConnect(self):
        self.ui.openAct.triggered.connect(partial(openAct, self.model, self.ui.openImageFileLabel))
        self.ui.saveAct.triggered.connect(partial(saveAct, self.model, self.ui.statusBar))
        self.ui.openFilePathAct.triggered.connect(partial(openFilePathAct, self.model, self.ui.openImageFileLabel))
        self.ui.exitAct.triggered.connect(QApplication.instance().quit)

    def opencvMenuConnect(self):
        self.ui.thresholdAct.triggered.connect((partial(thresholdAct, self.model, self.ui.tabLabel1)))

    def buttonConnect(self):
        self.ui.preImageButton.clicked.connect((partial(preImage, self.model, self.ui.openImageFileLabel)))
        self.ui.nextImageButton.clicked.connect((partial(nextImage, self.model, self.ui.openImageFileLabel)))
