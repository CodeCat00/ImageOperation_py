# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QToolBar, QVBoxLayout, QWidget)

class Ui_MainUi(object):
    def setupUi(self, MainUi):
        if not MainUi.objectName():
            MainUi.setObjectName(u"MainUi")
        MainUi.resize(1728, 1051)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainUi.sizePolicy().hasHeightForWidth())
        MainUi.setSizePolicy(sizePolicy)
        MainUi.setStyleSheet(u"\n"
"\n"
"                QWidget {\n"
"                background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #708090,stop:1 #C8C8D0);\n"
"                }\n"
"\n"
"                QMenuBar {\n"
"                min-width: 80px;\n"
"                min-height: 35px;\n"
"                }\n"
"\n"
"                QMenu {\n"
"                border-radius: 30px;\n"
"                }\n"
"                QMenu::item {\n"
"                min-width: 60px;\n"
"                min-height: 40px;\n"
"                padding: 2px 25px 2px 30px;\n"
"                margin-left: 5px;\n"
"                }\n"
"                QMenu::item:selected {\n"
"                border-width:1px;\n"
"                border-color: #516589;\n"
"                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(45,133,207), stop: 1.0\n"
"                rgb(125,195,250));\n"
"                color:#E6FFFF;\n"
"                }\n"
"\n"
"                QPushButton {\n"
"                min-width:100px;\n"
""
                        "                min-height:40px;\n"
"                border-radius:10px;\n"
"                }\n"
"\n"
"                QPushButton:hover\n"
"                {\n"
"                background-color:rgb(44 , 137 , 255);\n"
"                }\n"
"\n"
"                QPushButton:pressed\n"
"                {\n"
"                background-color:rgb(14 , 135 , 228);\n"
"                padding-left:3px;\n"
"                padding-top:3px;\n"
"                }\n"
"\n"
"                QScrollBar:horizontal {\n"
"                border: 1px solid #222222;\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #ffffff, stop: 0.5 #ffffff, stop: 1\n"
"                #ffffff);\n"
"                height: 7px;\n"
"                margin: 0px 16px 0 16px;\n"
"                }\n"
"                QScrollBar::handle:horizontal {\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #b1b1b1, stop: 0.5 #b3b3b3, stop: 1\n"
"                #b1b1b1);\n"
"       "
                        "         min-height: 20px;\n"
"                border-radius: 20px;\n"
"                }\n"
"                QScrollBar::add-line:horizontal {\n"
"                border: 1px solid #1b1b19;\n"
"                border-radius: 20px;\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #999999, stop: 1 #999999);\n"
"                width: 14px;\n"
"                subcontrol-position: right;\n"
"                subcontrol-origin: margin;\n"
"                }\n"
"                QScrollBar::sub-line:horizontal {\n"
"                border: 1px solid #1b1b19;\n"
"                border-radius: 20px;\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #999999, stop: 1 #999999);\n"
"                width: 14px;\n"
"                subcontrol-position: left;\n"
"                subcontrol-origin: margin;\n"
"                }\n"
"                QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal {\n"
"                border: 1px soli"
                        "d black;\n"
"                width: 1px;\n"
"                height: 1px;\n"
"                background: white;\n"
"                }\n"
"                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"                background: none;\n"
"                }\n"
"                QScrollBar:vertical {\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #ffffff, stop: 0.5 #ffffff, stop: 1\n"
"                #ffffff);\n"
"                width: 7px;\n"
"                margin: 16px 0 16px 0;\n"
"                border: 1px solid #222222;\n"
"                }\n"
"                QScrollBar::handle:vertical {\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b1b1b1, stop: 0.5 #b3b3b3, stop: 1\n"
"                #b1b1b1);\n"
"                min-height: 20px;\n"
"                border-radius: 20px;\n"
"                }\n"
"                QScrollBar::add-line:vertical {\n"
"                border: 1px solid #1b1b19;\n"
""
                        "                border-radius: 20px;\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #999999, stop: 1 #999999);\n"
"                height: 14px;\n"
"                subcontrol-position: bottom;\n"
"                subcontrol-origin: margin;\n"
"                }\n"
"                QScrollBar::sub-line:vertical {\n"
"                border: 1px solid #1b1b19;\n"
"                border-radius: 20px;\n"
"                background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #999999, stop: 1 #999999);\n"
"                height: 14px;\n"
"                subcontrol-position: top;\n"
"                subcontrol-origin: margin;\n"
"                }\n"
"                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"                border: 1px solid black;\n"
"                width: 1px;\n"
"                height: 1px;\n"
"                background: white;\n"
"                }\n"
"                QScrollBar::add-page:vertical, QScrollBar::sub-"
                        "page:vertical {\n"
"                background: none;\n"
"                }\n"
"\n"
"                QTabWidget::pane {\n"
"                border: 1px solid #444;\n"
"                top: 1px;\n"
"                }\n"
"\n"
"                QTabBar::tab {\n"
"                color: #ffffff;\n"
"                border: 1px solid #444;\n"
"                border-bottom-style: none;\n"
"                background-color: #999999;\n"
"                padding-left: 10px;\n"
"                padding-right: 10px;\n"
"                padding-top: 3px;\n"
"                padding-bottom: 2px;\n"
"                margin-right: -1px;\n"
"                min-width: 80px;\n"
"                min-height: 30px;\n"
"                }\n"
"                QTabBar::tab:last {\n"
"                margin-right: 0;\n"
"                border-top-right-radius: 3px;\n"
"                }\n"
"                QTabBar::tab:first:!selected {\n"
"                margin-left: 0px;\n"
"                border-top-left-radius: 3px;\n"
"       "
                        "         }\n"
"                QTabBar::tab:!selected {\n"
"                border-bottom-style: solid;\n"
"                margin-top: 3px;\n"
"                background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #1874CD, stop:.4 #737373);\n"
"                }\n"
"                QTabBar::tab:selected {\n"
"                border-top-left-radius: 3px;\n"
"                border-top-right-radius: 3px;\n"
"                margin-bottom: 0px;\n"
"                }\n"
"                QTabBar::tab:!selected:hover {\n"
"                border-top-left-radius: 3px;\n"
"                border-top-right-radius: 3px;\n"
"                background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #737373, stop:0.2\n"
"                #999999, stop:0.1 #b1b1b1);\n"
"                }\n"
"\n"
"            ")
        self.actionOpen = QAction(MainUi)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainUi)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setCheckable(False)
        self.actionSave.setEnabled(True)
        self.actionExit = QAction(MainUi)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpenFilePath = QAction(MainUi)
        self.actionOpenFilePath.setObjectName(u"actionOpenFilePath")
        self.actionGrayProcessing = QAction(MainUi)
        self.actionGrayProcessing.setObjectName(u"actionGrayProcessing")
        self.actionImageInversion = QAction(MainUi)
        self.actionImageInversion.setObjectName(u"actionImageInversion")
        self.actionLogarithmicTransformation = QAction(MainUi)
        self.actionLogarithmicTransformation.setObjectName(u"actionLogarithmicTransformation")
        self.actionGammaTransform = QAction(MainUi)
        self.actionGammaTransform.setObjectName(u"actionGammaTransform")
        self.actionHistogramEqualization = QAction(MainUi)
        self.actionHistogramEqualization.setObjectName(u"actionHistogramEqualization")
        self.actionSmoothSpatialFilter = QAction(MainUi)
        self.actionSmoothSpatialFilter.setObjectName(u"actionSmoothSpatialFilter")
        self.actionSharpeningSpatialFilter = QAction(MainUi)
        self.actionSharpeningSpatialFilter.setObjectName(u"actionSharpeningSpatialFilter")
        self.actionGaussianBlur = QAction(MainUi)
        self.actionGaussianBlur.setObjectName(u"actionGaussianBlur")
        self.actionMeanBlur = QAction(MainUi)
        self.actionMeanBlur.setObjectName(u"actionMeanBlur")
        self.actionMedianBlur = QAction(MainUi)
        self.actionMedianBlur.setObjectName(u"actionMedianBlur")
        self.actionSobel = QAction(MainUi)
        self.actionSobel.setObjectName(u"actionSobel")
        self.actionLaplacian = QAction(MainUi)
        self.actionLaplacian.setObjectName(u"actionLaplacian")
        self.actionGaussianNoise = QAction(MainUi)
        self.actionGaussianNoise.setObjectName(u"actionGaussianNoise")
        self.actionSaltAndPepperNoise = QAction(MainUi)
        self.actionSaltAndPepperNoise.setObjectName(u"actionSaltAndPepperNoise")
        self.actionBinaryImage = QAction(MainUi)
        self.actionBinaryImage.setObjectName(u"actionBinaryImage")
        self.actionCorrosion = QAction(MainUi)
        self.actionCorrosion.setObjectName(u"actionCorrosion")
        self.actionExpansion = QAction(MainUi)
        self.actionExpansion.setObjectName(u"actionExpansion")
        self.actionOpenOperation = QAction(MainUi)
        self.actionOpenOperation.setObjectName(u"actionOpenOperation")
        self.actionClosedOperation = QAction(MainUi)
        self.actionClosedOperation.setObjectName(u"actionClosedOperation")
        self.actionBoundaryExtraction = QAction(MainUi)
        self.actionBoundaryExtraction.setObjectName(u"actionBoundaryExtraction")
        self.actionHoleFilling = QAction(MainUi)
        self.actionHoleFilling.setObjectName(u"actionHoleFilling")
        self.actionOutlierDetection = QAction(MainUi)
        self.actionOutlierDetection.setObjectName(u"actionOutlierDetection")
        self.actionEdgeDetection = QAction(MainUi)
        self.actionEdgeDetection.setObjectName(u"actionEdgeDetection")
        self.actionAdaptiveThreshold = QAction(MainUi)
        self.actionAdaptiveThreshold.setObjectName(u"actionAdaptiveThreshold")
        self.actionWatershed = QAction(MainUi)
        self.actionWatershed.setObjectName(u"actionWatershed")
        self.centralWidget = QWidget(MainUi)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy1)
        self.centralWidget.setLayoutDirection(Qt.LeftToRight)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setInputMethodHints(Qt.ImhNone)
        self.horizontalLayout_5 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.openImageVerticalLayout = QVBoxLayout()
        self.openImageVerticalLayout.setSpacing(6)
        self.openImageVerticalLayout.setObjectName(u"openImageVerticalLayout")
        self.openImageButtonHorizontalLayout = QHBoxLayout()
        self.openImageButtonHorizontalLayout.setSpacing(6)
        self.openImageButtonHorizontalLayout.setObjectName(u"openImageButtonHorizontalLayout")
        self.preImageButton = QPushButton(self.centralWidget)
        self.preImageButton.setObjectName(u"preImageButton")
        self.preImageButton.setAutoRepeat(False)
        self.preImageButton.setAutoDefault(False)
        self.preImageButton.setFlat(False)

        self.openImageButtonHorizontalLayout.addWidget(self.preImageButton)

        self.openImageHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.openImageButtonHorizontalLayout.addItem(self.openImageHorizontalSpacer)

        self.nextImageButton = QPushButton(self.centralWidget)
        self.nextImageButton.setObjectName(u"nextImageButton")
        self.nextImageButton.setFlat(False)

        self.openImageButtonHorizontalLayout.addWidget(self.nextImageButton)


        self.openImageVerticalLayout.addLayout(self.openImageButtonHorizontalLayout)

        self.openImageFileScroll = QScrollArea(self.centralWidget)
        self.openImageFileScroll.setObjectName(u"openImageFileScroll")
        self.openImageFileScroll.setLayoutDirection(Qt.LeftToRight)
        self.openImageFileScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.openImageFileScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.openImageFileScroll.setWidgetResizable(True)
        self.openImageFileScroll.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.openImageFileScrollWidget = QWidget()
        self.openImageFileScrollWidget.setObjectName(u"openImageFileScrollWidget")
        self.openImageFileScrollWidget.setGeometry(QRect(0, 0, 840, 894))
        self.openImageFileScrollWidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self.openImageFileScrollWidget)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.openImageFileLabel = QLabel(self.openImageFileScrollWidget)
        self.openImageFileLabel.setObjectName(u"openImageFileLabel")
        self.openImageFileLabel.setLayoutDirection(Qt.LeftToRight)
        self.openImageFileLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.openImageFileLabel)

        self.openImageFileScroll.setWidget(self.openImageFileScrollWidget)

        self.openImageVerticalLayout.addWidget(self.openImageFileScroll)


        self.horizontalLayout_5.addLayout(self.openImageVerticalLayout)

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget1 = QWidget()
        self.tabWidget1.setObjectName(u"tabWidget1")
        self.horizontalLayout_2 = QHBoxLayout(self.tabWidget1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabScrollArea1 = QScrollArea(self.tabWidget1)
        self.tabScrollArea1.setObjectName(u"tabScrollArea1")
        self.tabScrollArea1.setWidgetResizable(True)
        self.tabInnerWidget1 = QWidget()
        self.tabInnerWidget1.setObjectName(u"tabInnerWidget1")
        self.tabInnerWidget1.setGeometry(QRect(0, 0, 800, 879))
        self.verticalLayout = QVBoxLayout(self.tabInnerWidget1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabLabel1 = QLabel(self.tabInnerWidget1)
        self.tabLabel1.setObjectName(u"tabLabel1")
        self.tabLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.tabLabel1)

        self.tabScrollArea1.setWidget(self.tabInnerWidget1)

        self.horizontalLayout_2.addWidget(self.tabScrollArea1)

        self.tabWidget.addTab(self.tabWidget1, "")
        self.tabWidget2 = QWidget()
        self.tabWidget2.setObjectName(u"tabWidget2")
        self.horizontalLayout_3 = QHBoxLayout(self.tabWidget2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabScrollArea2 = QScrollArea(self.tabWidget2)
        self.tabScrollArea2.setObjectName(u"tabScrollArea2")
        self.tabScrollArea2.setWidgetResizable(True)
        self.tabInnerWidget2 = QWidget()
        self.tabInnerWidget2.setObjectName(u"tabInnerWidget2")
        self.tabInnerWidget2.setGeometry(QRect(0, 0, 800, 879))
        self.verticalLayout_2 = QVBoxLayout(self.tabInnerWidget2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabLabel2 = QLabel(self.tabInnerWidget2)
        self.tabLabel2.setObjectName(u"tabLabel2")
        self.tabLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.tabLabel2)

        self.tabScrollArea2.setWidget(self.tabInnerWidget2)

        self.horizontalLayout_3.addWidget(self.tabScrollArea2)

        self.tabWidget.addTab(self.tabWidget2, "")
        self.tabWidget3 = QWidget()
        self.tabWidget3.setObjectName(u"tabWidget3")
        self.tabWidget3.setFocusPolicy(Qt.NoFocus)
        self.horizontalLayout = QHBoxLayout(self.tabWidget3)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.tabWidget3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.tabInnerWidget3 = QWidget()
        self.tabInnerWidget3.setObjectName(u"tabInnerWidget3")
        self.tabInnerWidget3.setGeometry(QRect(0, 0, 800, 879))
        self.verticalLayout_3 = QVBoxLayout(self.tabInnerWidget3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabLabel3 = QLabel(self.tabInnerWidget3)
        self.tabLabel3.setObjectName(u"tabLabel3")

        self.verticalLayout_3.addWidget(self.tabLabel3)

        self.scrollArea.setWidget(self.tabInnerWidget3)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tabWidget3, "")
        self.tabWidget4 = QWidget()
        self.tabWidget4.setObjectName(u"tabWidget4")
        self.horizontalLayout_6 = QHBoxLayout(self.tabWidget4)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scrollArea_2 = QScrollArea(self.tabWidget4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.tabInnerWidget4 = QWidget()
        self.tabInnerWidget4.setObjectName(u"tabInnerWidget4")
        self.tabInnerWidget4.setGeometry(QRect(0, 0, 800, 879))
        self.verticalLayout_4 = QVBoxLayout(self.tabInnerWidget4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabLabel4 = QLabel(self.tabInnerWidget4)
        self.tabLabel4.setObjectName(u"tabLabel4")

        self.verticalLayout_4.addWidget(self.tabLabel4)

        self.scrollArea_2.setWidget(self.tabInnerWidget4)

        self.horizontalLayout_6.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tabWidget4, "")
        self.tabWidget5 = QWidget()
        self.tabWidget5.setObjectName(u"tabWidget5")
        self.horizontalLayout_7 = QHBoxLayout(self.tabWidget5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea_3 = QScrollArea(self.tabWidget5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.tabInnerWidget5 = QWidget()
        self.tabInnerWidget5.setObjectName(u"tabInnerWidget5")
        self.tabInnerWidget5.setGeometry(QRect(0, 0, 800, 879))
        self.verticalLayout_5 = QVBoxLayout(self.tabInnerWidget5)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tabInnerWidget5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.scrollArea_3.setWidget(self.tabInnerWidget5)

        self.horizontalLayout_7.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.tabWidget5, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        MainUi.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainUi)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1728, 37))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpenCV = QMenu(self.menuBar)
        self.menuOpenCV.setObjectName(u"menuOpenCV")
        self.menuColorAdjustment = QMenu(self.menuOpenCV)
        self.menuColorAdjustment.setObjectName(u"menuColorAdjustment")
        self.menuImageBlur = QMenu(self.menuOpenCV)
        self.menuImageBlur.setObjectName(u"menuImageBlur")
        self.menuNoise = QMenu(self.menuOpenCV)
        self.menuNoise.setObjectName(u"menuNoise")
        self.menuMorphology = QMenu(self.menuOpenCV)
        self.menuMorphology.setObjectName(u"menuMorphology")
        self.menuImageSegmentation = QMenu(self.menuOpenCV)
        self.menuImageSegmentation.setObjectName(u"menuImageSegmentation")
        MainUi.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainUi)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainUi.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainUi)
        self.statusBar.setObjectName(u"statusBar")
        MainUi.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOpenCV.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpenFilePath)
        self.menuFile.addAction(self.actionExit)
        self.menuOpenCV.addAction(self.menuColorAdjustment.menuAction())
        self.menuOpenCV.addAction(self.menuImageBlur.menuAction())
        self.menuOpenCV.addAction(self.menuNoise.menuAction())
        self.menuOpenCV.addAction(self.menuMorphology.menuAction())
        self.menuOpenCV.addAction(self.menuImageSegmentation.menuAction())
        self.menuColorAdjustment.addAction(self.actionGrayProcessing)
        self.menuColorAdjustment.addAction(self.actionImageInversion)
        self.menuColorAdjustment.addAction(self.actionLogarithmicTransformation)
        self.menuColorAdjustment.addAction(self.actionGammaTransform)
        self.menuColorAdjustment.addAction(self.actionHistogramEqualization)
        self.menuColorAdjustment.addAction(self.actionSmoothSpatialFilter)
        self.menuColorAdjustment.addAction(self.actionSharpeningSpatialFilter)
        self.menuImageBlur.addAction(self.actionGaussianBlur)
        self.menuImageBlur.addAction(self.actionMeanBlur)
        self.menuImageBlur.addAction(self.actionMedianBlur)
        self.menuImageBlur.addAction(self.actionSobel)
        self.menuImageBlur.addAction(self.actionLaplacian)
        self.menuNoise.addAction(self.actionGaussianNoise)
        self.menuNoise.addAction(self.actionSaltAndPepperNoise)
        self.menuMorphology.addAction(self.actionBinaryImage)
        self.menuMorphology.addAction(self.actionCorrosion)
        self.menuMorphology.addAction(self.actionExpansion)
        self.menuMorphology.addAction(self.actionOpenOperation)
        self.menuMorphology.addAction(self.actionClosedOperation)
        self.menuMorphology.addAction(self.actionBoundaryExtraction)
        self.menuMorphology.addAction(self.actionHoleFilling)
        self.menuImageSegmentation.addAction(self.actionOutlierDetection)
        self.menuImageSegmentation.addAction(self.actionEdgeDetection)
        self.menuImageSegmentation.addAction(self.actionAdaptiveThreshold)
        self.menuImageSegmentation.addAction(self.actionWatershed)

        self.retranslateUi(MainUi)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainUi)
    # setupUi

    def retranslateUi(self, MainUi):
        MainUi.setWindowTitle(QCoreApplication.translate("MainUi", u"ImageOperationModel", None))
        self.actionOpen.setText(QCoreApplication.translate("MainUi", u"\u6253\u5f00\u56fe\u7247", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainUi", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainUi", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainUi", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainUi", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainUi", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenFilePath.setText(QCoreApplication.translate("MainUi", u"\u8bfb\u53d6\u6587\u4ef6\u5939", None))
        self.actionGrayProcessing.setText(QCoreApplication.translate("MainUi", u"\u7070\u5ea6\u5904\u7406", None))
        self.actionImageInversion.setText(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u53cd\u8f6c", None))
        self.actionLogarithmicTransformation.setText(QCoreApplication.translate("MainUi", u"\u5bf9\u6570\u53d8\u6362", None))
        self.actionGammaTransform.setText(QCoreApplication.translate("MainUi", u"\u4f3d\u9a6c\u53d8\u6362", None))
        self.actionHistogramEqualization.setText(QCoreApplication.translate("MainUi", u"\u76f4\u65b9\u56fe\u5747\u8861\u5316", None))
        self.actionSmoothSpatialFilter.setText(QCoreApplication.translate("MainUi", u"\u5e73\u6ed1\u7a7a\u95f4\u6ee4\u6ce2\u5668", None))
        self.actionSharpeningSpatialFilter.setText(QCoreApplication.translate("MainUi", u"\u9510\u5316\u7a7a\u95f4\u6ee4\u6ce2\u5668", None))
        self.actionGaussianBlur.setText(QCoreApplication.translate("MainUi", u"\u4f4e\u901a\u6ee4\u6ce2\u5668", None))
        self.actionMeanBlur.setText(QCoreApplication.translate("MainUi", u"\u5747\u503c\u6ee4\u6ce2\u5668", None))
        self.actionMedianBlur.setText(QCoreApplication.translate("MainUi", u"\u4e2d\u503c\u6ee4\u6ce2\u5668", None))
        self.actionSobel.setText(QCoreApplication.translate("MainUi", u"\u65b9\u5411\u6ee4\u6ce2\u5668", None))
        self.actionLaplacian.setText(QCoreApplication.translate("MainUi", u"\u62c9\u666e\u62c9\u65af\u53d8\u6362", None))
        self.actionGaussianNoise.setText(QCoreApplication.translate("MainUi", u"\u9ad8\u65af\u566a\u58f0", None))
        self.actionSaltAndPepperNoise.setText(QCoreApplication.translate("MainUi", u"\u6912\u76d0\u566a\u58f0", None))
        self.actionBinaryImage.setText(QCoreApplication.translate("MainUi", u"\u4e8c\u503c\u56fe\u50cf", None))
        self.actionCorrosion.setText(QCoreApplication.translate("MainUi", u"\u8150\u8680", None))
        self.actionExpansion.setText(QCoreApplication.translate("MainUi", u"\u81a8\u80c0", None))
        self.actionOpenOperation.setText(QCoreApplication.translate("MainUi", u"\u5f00\u64cd\u4f5c", None))
        self.actionClosedOperation.setText(QCoreApplication.translate("MainUi", u"\u95ed\u64cd\u4f5c", None))
        self.actionBoundaryExtraction.setText(QCoreApplication.translate("MainUi", u"\u8fb9\u754c\u63d0\u53d6", None))
        self.actionHoleFilling.setText(QCoreApplication.translate("MainUi", u"\u5b54\u6d1e\u586b\u5145", None))
        self.actionOutlierDetection.setText(QCoreApplication.translate("MainUi", u"\u5b64\u7acb\u70b9\u68c0\u6d4b", None))
        self.actionEdgeDetection.setText(QCoreApplication.translate("MainUi", u"\u8fb9\u7f18\u68c0\u6d4b", None))
        self.actionAdaptiveThreshold.setText(QCoreApplication.translate("MainUi", u"\u81ea\u9002\u5e94\u9608\u503c", None))
        self.actionWatershed.setText(QCoreApplication.translate("MainUi", u"\u5206\u6c34\u5cad", None))
        self.preImageButton.setText(QCoreApplication.translate("MainUi", u"\u4e0a\u4e00\u5f20", None))
        self.nextImageButton.setText(QCoreApplication.translate("MainUi", u"\u4e0b\u4e00\u5f20", None))
        self.openImageFileLabel.setText("")
        self.tabLabel1.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget1), QCoreApplication.translate("MainUi", u"Tab1", None))
        self.tabLabel2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget2), QCoreApplication.translate("MainUi", u"Tab2", None))
        self.tabLabel3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget3), QCoreApplication.translate("MainUi", u"Tab3", None))
        self.tabLabel4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget4), QCoreApplication.translate("MainUi", u"Tab4", None))
        self.label_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget5), QCoreApplication.translate("MainUi", u"Tab5", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainUi", u"\u6587\u4ef6", None))
        self.menuOpenCV.setTitle(QCoreApplication.translate("MainUi", u"OpenCV\u793a\u4f8b", None))
        self.menuColorAdjustment.setTitle(QCoreApplication.translate("MainUi", u"\u8272\u5f69\u8c03\u6574", None))
        self.menuImageBlur.setTitle(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u6ee4\u6ce2\u5668", None))
        self.menuNoise.setTitle(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u566a\u58f0", None))
        self.menuMorphology.setTitle(QCoreApplication.translate("MainUi", u"\u5f62\u6001\u5b66", None))
        self.menuImageSegmentation.setTitle(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u5206\u5272", None))
    # retranslateUi

