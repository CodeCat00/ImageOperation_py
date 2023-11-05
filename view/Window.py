from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication

from control.action.FileMenuAction import openAct, thresholdAct
from model.ImageOperationmodel import ImageOperationModel
from view.ui.Ui_MainUi import Ui_MainUi


class Window(QMainWindow):

    def __init__(self, model=ImageOperationModel):
        # super
        super().__init__()
        # 从文件中加载界面
        self.loadUi()
        # 关联槽函数
        self.fileMenuConnect(model)
        self.opencvMenuConnect(model)

    def loadUi(self):
        self.ui = Ui_MainUi()
        self.ui.setupUi(self)

    def fileMenuConnect(self, model):
        self.ui.openAct.triggered.connect(partial(openAct, model, self.ui.openImageFileLabel))
        self.ui.saveAct.triggered.connect(QApplication.instance().quit)
        self.ui.exitAct.triggered.connect(QApplication.instance().quit)
        self.ui.openFilePathAct.triggered.connect(QApplication.instance().quit)
        self.ui.saveFilePathAct.triggered.connect(QApplication.instance().quit)

    def opencvMenuConnect(self, model):
        self.ui.thresholdAct.triggered.connect((partial(thresholdAct, model, self.ui.tabLabel1)))
