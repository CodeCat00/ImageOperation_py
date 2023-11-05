from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication

from control.action.ButtonAction import preImage, nextImage
from control.action.FileMenuAction import openAct, saveAct, openFilePathAct
from control.action.OpenCVAction import thresholdAct, blurAct, gaussianBlurAct, medianBlurAct, bilateralFilterAct, \
    morphologyExOpenAct, morphologyExCloseAct, morphologyExGradientAct, morphologyExTophatAct, morphologyExBlackhatAct, \
    sobelAct, cannyAct, dilateAct, findContoursAct, equalizeHistAct, createCLAHEAct, houghLinesAct, houghLinesPAct, \
    houghCirclesAct, watershedAct, grabCutAct
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
        self.ui.blurAct.triggered.connect((partial(blurAct, self.model, self.ui.tabLabel1)))
        self.ui.sobelAct.triggered.connect((partial(sobelAct, self.model, self.ui.tabLabel1)))
        self.ui.cannyAct.triggered.connect((partial(cannyAct, self.model, self.ui.tabLabel1)))
        self.ui.dilateAct.triggered.connect((partial(dilateAct, self.model, self.ui.tabLabel1)))
        self.ui.grabCutAct.triggered.connect((partial(grabCutAct, self.model, self.ui.tabLabel1)))
        self.ui.watershedAct.triggered.connect((partial(watershedAct, self.model, self.ui.tabLabel1)))
        self.ui.thresholdAct.triggered.connect((partial(thresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.medianBlurAct.triggered.connect((partial(medianBlurAct, self.model, self.ui.tabLabel1)))
        self.ui.createCLAHEAct.triggered.connect((partial(createCLAHEAct, self.model, self.ui.tabLabel1)))
        self.ui.houghLinesPAct.triggered.connect((partial(houghLinesPAct, self.model, self.ui.tabLabel1)))
        self.ui.findContoursAct.triggered.connect((partial(findContoursAct, self.model, self.ui.tabLabel1)))
        self.ui.gaussianBlurAct.triggered.connect((partial(gaussianBlurAct, self.model, self.ui.tabLabel1)))
        self.ui.equalizeHistAct.triggered.connect((partial(equalizeHistAct, self.model, self.ui.tabLabel1)))
        self.ui.houghCirclesAct.triggered.connect((partial(houghCirclesAct, self.model, self.ui.tabLabel1)))
        self.ui.bilateralFilterAct.triggered.connect((partial(bilateralFilterAct, self.model, self.ui.tabLabel1)))
        self.ui.morphologyExOpenAct.triggered.connect((partial(morphologyExOpenAct, self.model, self.ui.tabLabel1)))
        self.ui.morphologyExCloseAct.triggered.connect((partial(morphologyExCloseAct, self.model, self.ui.tabLabel1)))
        self.ui.morphologyExGradientAct.triggered.connect(
            (partial(morphologyExGradientAct, self.model, self.ui.tabLabel1)))
        self.ui.morphologyExBlackhatAct.triggered.connect(
            (partial(morphologyExBlackhatAct, self.model, self.ui.tabLabel1)))

    def buttonConnect(self):
        self.ui.preImageButton.clicked.connect((partial(preImage, self.model, self.ui.openImageFileLabel)))
        self.ui.nextImageButton.clicked.connect((partial(nextImage, self.model, self.ui.openImageFileLabel)))
