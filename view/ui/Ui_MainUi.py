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
        self.actionResize = QAction(MainUi)
        self.actionResize.setObjectName(u"actionResize")
        self.actionTranslation = QAction(MainUi)
        self.actionTranslation.setObjectName(u"actionTranslation")
        self.actionRotation = QAction(MainUi)
        self.actionRotation.setObjectName(u"actionRotation")
        self.actionWarpAffine = QAction(MainUi)
        self.actionWarpAffine.setObjectName(u"actionWarpAffine")
        self.actionWarpPerspective = QAction(MainUi)
        self.actionWarpPerspective.setObjectName(u"actionWarpPerspective")
        self.actionSimpleBinaryThreshold = QAction(MainUi)
        self.actionSimpleBinaryThreshold.setObjectName(u"actionSimpleBinaryThreshold")
        self.actionSimpleBinaryInvThreshold = QAction(MainUi)
        self.actionSimpleBinaryInvThreshold.setObjectName(u"actionSimpleBinaryInvThreshold")
        self.actionSimpleTruncThreshold = QAction(MainUi)
        self.actionSimpleTruncThreshold.setObjectName(u"actionSimpleTruncThreshold")
        self.actionSimpleToZeroThreshold = QAction(MainUi)
        self.actionSimpleToZeroThreshold.setObjectName(u"actionSimpleToZeroThreshold")
        self.actionSimpleToZeroInvThreshold = QAction(MainUi)
        self.actionSimpleToZeroInvThreshold.setObjectName(u"actionSimpleToZeroInvThreshold")
        self.actionAdaptiveMeanThreshold = QAction(MainUi)
        self.actionAdaptiveMeanThreshold.setObjectName(u"actionAdaptiveMeanThreshold")
        self.actionAdaptiveGaussianThreshold = QAction(MainUi)
        self.actionAdaptiveGaussianThreshold.setObjectName(u"actionAdaptiveGaussianThreshold")
        self.actionOTSUThreshold = QAction(MainUi)
        self.actionOTSUThreshold.setObjectName(u"actionOTSUThreshold")
        self.actionFilter2D = QAction(MainUi)
        self.actionFilter2D.setObjectName(u"actionFilter2D")
        self.actionBlur = QAction(MainUi)
        self.actionBlur.setObjectName(u"actionBlur")
        self.actionGaussianBlur = QAction(MainUi)
        self.actionGaussianBlur.setObjectName(u"actionGaussianBlur")
        self.actionMedianBlur = QAction(MainUi)
        self.actionMedianBlur.setObjectName(u"actionMedianBlur")
        self.actionBilateralFilter = QAction(MainUi)
        self.actionBilateralFilter.setObjectName(u"actionBilateralFilter")
        self.actionErosion = QAction(MainUi)
        self.actionErosion.setObjectName(u"actionErosion")
        self.actionDilate = QAction(MainUi)
        self.actionDilate.setObjectName(u"actionDilate")
        self.actionMorphologyExOpen = QAction(MainUi)
        self.actionMorphologyExOpen.setObjectName(u"actionMorphologyExOpen")
        self.actionMorphologyExClose = QAction(MainUi)
        self.actionMorphologyExClose.setObjectName(u"actionMorphologyExClose")
        self.actionMorphologyExGradient = QAction(MainUi)
        self.actionMorphologyExGradient.setObjectName(u"actionMorphologyExGradient")
        self.actionMorphologyExTopHat = QAction(MainUi)
        self.actionMorphologyExTopHat.setObjectName(u"actionMorphologyExTopHat")
        self.actionMorphologyExBlackHat = QAction(MainUi)
        self.actionMorphologyExBlackHat.setObjectName(u"actionMorphologyExBlackHat")
        self.actionLaplacian = QAction(MainUi)
        self.actionLaplacian.setObjectName(u"actionLaplacian")
        self.actionSobelX = QAction(MainUi)
        self.actionSobelX.setObjectName(u"actionSobelX")
        self.actionSobelY = QAction(MainUi)
        self.actionSobelY.setObjectName(u"actionSobelY")
        self.actionCanny = QAction(MainUi)
        self.actionCanny.setObjectName(u"actionCanny")
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
        self.tabInnerWidget2.setGeometry(QRect(0, 0, 83, 40))
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
        self.tabInnerWidget3.setGeometry(QRect(0, 0, 83, 40))
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
        self.tabInnerWidget4.setGeometry(QRect(0, 0, 83, 40))
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
        self.tabInnerWidget5.setGeometry(QRect(0, 0, 83, 40))
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
        self.menuGeometricTransformation = QMenu(self.menuOpenCV)
        self.menuGeometricTransformation.setObjectName(u"menuGeometricTransformation")
        self.menuImageThreshold = QMenu(self.menuOpenCV)
        self.menuImageThreshold.setObjectName(u"menuImageThreshold")
        self.menu = QMenu(self.menuOpenCV)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuOpenCV)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuOpenCV)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menuOpenCV)
        self.menu_4.setObjectName(u"menu_4")
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
        self.menuOpenCV.addAction(self.menuGeometricTransformation.menuAction())
        self.menuOpenCV.addAction(self.menuImageThreshold.menuAction())
        self.menuOpenCV.addAction(self.menu.menuAction())
        self.menuOpenCV.addAction(self.menu_2.menuAction())
        self.menuOpenCV.addAction(self.menu_3.menuAction())
        self.menuOpenCV.addAction(self.menu_4.menuAction())
        self.menuGeometricTransformation.addAction(self.actionResize)
        self.menuGeometricTransformation.addAction(self.actionTranslation)
        self.menuGeometricTransformation.addAction(self.actionRotation)
        self.menuGeometricTransformation.addAction(self.actionWarpAffine)
        self.menuGeometricTransformation.addAction(self.actionWarpPerspective)
        self.menuImageThreshold.addAction(self.actionSimpleBinaryThreshold)
        self.menuImageThreshold.addAction(self.actionSimpleBinaryInvThreshold)
        self.menuImageThreshold.addAction(self.actionSimpleTruncThreshold)
        self.menuImageThreshold.addAction(self.actionSimpleToZeroThreshold)
        self.menuImageThreshold.addAction(self.actionSimpleToZeroInvThreshold)
        self.menuImageThreshold.addAction(self.actionAdaptiveMeanThreshold)
        self.menuImageThreshold.addAction(self.actionAdaptiveGaussianThreshold)
        self.menuImageThreshold.addAction(self.actionOTSUThreshold)
        self.menu.addAction(self.actionFilter2D)
        self.menu.addAction(self.actionBlur)
        self.menu.addAction(self.actionGaussianBlur)
        self.menu.addAction(self.actionMedianBlur)
        self.menu.addAction(self.actionBilateralFilter)
        self.menu_2.addAction(self.actionErosion)
        self.menu_2.addAction(self.actionDilate)
        self.menu_2.addAction(self.actionMorphologyExOpen)
        self.menu_2.addAction(self.actionMorphologyExClose)
        self.menu_2.addAction(self.actionMorphologyExGradient)
        self.menu_2.addAction(self.actionMorphologyExTopHat)
        self.menu_2.addAction(self.actionMorphologyExBlackHat)
        self.menu_3.addAction(self.actionLaplacian)
        self.menu_3.addAction(self.actionSobelX)
        self.menu_3.addAction(self.actionSobelY)
        self.menu_4.addAction(self.actionCanny)

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
        self.actionResize.setText(QCoreApplication.translate("MainUi", u"\u7f29\u653e", None))
        self.actionTranslation.setText(QCoreApplication.translate("MainUi", u"\u5e73\u79fb", None))
        self.actionRotation.setText(QCoreApplication.translate("MainUi", u"\u65cb\u8f6c", None))
        self.actionWarpAffine.setText(QCoreApplication.translate("MainUi", u"\u4eff\u5c04\u53d8\u6362", None))
        self.actionWarpPerspective.setText(QCoreApplication.translate("MainUi", u"\u900f\u89c6\u53d8\u6362", None))
        self.actionSimpleBinaryThreshold.setText(QCoreApplication.translate("MainUi", u"\u7b80\u5355\u4e8c\u503c\u5316\u9608\u503c", None))
        self.actionSimpleBinaryInvThreshold.setText(QCoreApplication.translate("MainUi", u"\u7b80\u5355\u53cd\u4e8c\u503c\u5316\u9608\u503c", None))
        self.actionSimpleTruncThreshold.setText(QCoreApplication.translate("MainUi", u"\u7b80\u5355\u622a\u65ad\u9608\u503c", None))
        self.actionSimpleToZeroThreshold.setText(QCoreApplication.translate("MainUi", u"\u7b80\u5355\u7f6e\u96f6\u9608\u503c", None))
        self.actionSimpleToZeroInvThreshold.setText(QCoreApplication.translate("MainUi", u"\u7b80\u5355\u7f6e\u96f6\u53cd\u9608\u503c", None))
        self.actionAdaptiveMeanThreshold.setText(QCoreApplication.translate("MainUi", u"\u81ea\u9002\u5e94\u5747\u503c\u9608\u503c", None))
        self.actionAdaptiveGaussianThreshold.setText(QCoreApplication.translate("MainUi", u"\u81ea\u9002\u5e94\u9ad8\u65af\u9608\u503c", None))
        self.actionOTSUThreshold.setText(QCoreApplication.translate("MainUi", u"OTSU\u4e8c\u503c\u5316", None))
        self.actionFilter2D.setText(QCoreApplication.translate("MainUi", u"\u4e8c\u7ef4\u5377\u79ef", None))
        self.actionBlur.setText(QCoreApplication.translate("MainUi", u"\u5747\u503c\u6a21\u7cca", None))
        self.actionGaussianBlur.setText(QCoreApplication.translate("MainUi", u"\u9ad8\u65af\u6a21\u7cca", None))
        self.actionMedianBlur.setText(QCoreApplication.translate("MainUi", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.actionBilateralFilter.setText(QCoreApplication.translate("MainUi", u"\u53cc\u8fb9\u6ee4\u6ce2", None))
        self.actionErosion.setText(QCoreApplication.translate("MainUi", u"\u8150\u8680", None))
        self.actionDilate.setText(QCoreApplication.translate("MainUi", u"\u81a8\u80c0", None))
        self.actionMorphologyExOpen.setText(QCoreApplication.translate("MainUi", u"\u5f00\u8fd0\u7b97", None))
        self.actionMorphologyExClose.setText(QCoreApplication.translate("MainUi", u"\u95ed\u8fd0\u7b97", None))
        self.actionMorphologyExGradient.setText(QCoreApplication.translate("MainUi", u"\u5f62\u6001\u68af\u5ea6", None))
        self.actionMorphologyExTopHat.setText(QCoreApplication.translate("MainUi", u"\u9876\u5e3d", None))
        self.actionMorphologyExBlackHat.setText(QCoreApplication.translate("MainUi", u"\u9ed1\u5e3d", None))
        self.actionLaplacian.setText(QCoreApplication.translate("MainUi", u"Laplacian\u5fae\u5206", None))
        self.actionSobelX.setText(QCoreApplication.translate("MainUi", u"SobelX\u8f74\u68af\u5ea6", None))
        self.actionSobelY.setText(QCoreApplication.translate("MainUi", u"SobelY\u8f74\u68af\u5ea6", None))
        self.actionCanny.setText(QCoreApplication.translate("MainUi", u"Canny", None))
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
        self.menuGeometricTransformation.setTitle(QCoreApplication.translate("MainUi", u"\u51e0\u4f55\u53d8\u6362", None))
        self.menuImageThreshold.setTitle(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u9608\u503c", None))
        self.menu.setTitle(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u5149\u6ed1", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainUi", u"\u5f62\u6001\u8f6c\u6362", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainUi", u"\u68af\u5ea6", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainUi", u"\u8fb9\u7f18\u68c0\u6d4b", None))
    # retranslateUi

