from functools import partial

from PySide6.QtWidgets import QMainWindow, QApplication

from control.action.ButtonAction import preImage, nextImage
from control.action.FileMenuMenu import openAct, saveAct, openFilePathAct
from control.action.GeometricTransformationMenu import resizeAct, translationAct, rotationAct, warpAffineAct, \
    warpPerspectiveAct
from control.action.ImageSmoothMenu import filter2DAct, blurAct, gaussianBlurAct, medianBlurAct, bilateralFilterAct
from control.action.ImageThresholdMenu import simpleBinaryThresholdAct, simpleTruncThresholdAct, \
    simpleBinaryInvThresholdAct, simpleToZeroThresholdAct, simpleToZeroInvThresholdAct, adaptiveMeanThresholdAct, \
    adaptiveGaussianThresholdAct, OTSUThresholdAct
from control.action.MorphologicalTransformationMenu import erosionAct, morphologyExOpenAct, dilateAct, \
    morphologyExCloseAct, morphologyExGradientAct, morphologyExTopHatAct, morphologyExBlackHatAct
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
        self.geometricTransformationMenuConnect()
        self.imageThresholdMenuConnect()
        self.morphologicalTransformationConnect()

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

    # 几何变换
    def geometricTransformationMenuConnect(self):
        self.ui.actionResize.triggered.connect((partial(resizeAct, self.model, self.ui.tabLabel1)))
        self.ui.actionTranslation.triggered.connect((partial(translationAct, self.model, self.ui.tabLabel1)))
        self.ui.actionRotation.triggered.connect((partial(rotationAct, self.model, self.ui.tabLabel1)))
        self.ui.actionWarpAffine.triggered.connect((partial(warpAffineAct, self.model, self.ui.tabLabel1)))
        self.ui.actionWarpPerspective.triggered.connect((partial(warpPerspectiveAct, self.model, self.ui.tabLabel1)))

    # 图像阈值
    def imageThresholdMenuConnect(self):
        self.ui.actionSimpleBinaryThreshold.triggered.connect(
            (partial(simpleBinaryThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionSimpleBinaryInvThreshold.triggered.connect(
            (partial(simpleBinaryInvThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionSimpleTruncThreshold.triggered.connect(
            (partial(simpleTruncThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionSimpleToZeroThreshold.triggered.connect(
            (partial(simpleToZeroThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionSimpleToZeroInvThreshold.triggered.connect(
            (partial(simpleToZeroInvThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionAdaptiveMeanThreshold.triggered.connect(
            (partial(adaptiveMeanThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionAdaptiveGaussianThreshold.triggered.connect(
            (partial(adaptiveGaussianThresholdAct, self.model, self.ui.tabLabel1)))
        self.ui.actionOTSUThreshold.triggered.connect(
            (partial(OTSUThresholdAct, self.model, self.ui.tabLabel1)))

    # 图像光滑
    def geometricTransformationMenuConnect(self):
        self.ui.actionFilter2D.triggered.connect((partial(filter2DAct, self.model, self.ui.tabLabel1)))
        self.ui.actionBlur.triggered.connect((partial(blurAct, self.model, self.ui.tabLabel1)))
        self.ui.actionGaussianBlur.triggered.connect((partial(gaussianBlurAct, self.model, self.ui.tabLabel1)))
        self.ui.actionMedianBlur.triggered.connect((partial(medianBlurAct, self.model, self.ui.tabLabel1)))
        self.ui.actionBilateralFilter.triggered.connect((partial(bilateralFilterAct, self.model, self.ui.tabLabel1)))

    # 形态转换
    def morphologicalTransformationConnect(self):
        self.ui.actionErosion.triggered.connect((partial(erosionAct, self.model, self.ui.tabLabel1)))
        self.ui.actionDilate.triggered.connect((partial(dilateAct, self.model, self.ui.tabLabel1)))
        self.ui.actionDilate.triggered.connect((partial(morphologyExOpenAct, self.model, self.ui.tabLabel1)))
        self.ui.actionMorphologyExClose.triggered.connect(
            (partial(morphologyExCloseAct, self.model, self.ui.tabLabel1)))
        self.ui.actionMorphologyExOpen.triggered.connect(
            (partial(morphologyExGradientAct, self.model, self.ui.tabLabel1)))
        self.ui.actionMorphologyExTopHat.triggered.connect(
            (partial(morphologyExTopHatAct, self.model, self.ui.tabLabel1)))
        self.ui.actionMorphologyExBlackHat.triggered.connect(
            (partial(morphologyExBlackHatAct, self.model, self.ui.tabLabel1)))
