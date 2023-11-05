# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
        MainUi.resize(1920, 1027)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainUi.sizePolicy().hasHeightForWidth())
        MainUi.setSizePolicy(sizePolicy)
        MainUi.setStyleSheet(u"\n"
"\n"
"QWidget {\n"
"       background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #708090,stop:1 #C8C8D0);\n"
"       }\n"
"\n"
"QMenuBar {\n"
"       min-width: 80px;\n"
"       min-height: 35px;\n"
"       }\n"
"\n"
"QMenu {\n"
"       border-radius: 30px;\n"
"       }\n"
"QMenu::item {\n"
"       min-width: 60px;\n"
"       min-height: 40px;\n"
"       padding: 2px 25px 2px 30px;\n"
"       margin-left: 5px;\n"
"       }\n"
"QMenu::item:selected {\n"
"       border-width:1px;\n"
"       border-color: #516589;\n"
"       background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(45,133,207), stop: 1.0 rgb(125,195,250));\n"
"       color:#E6FFFF;\n"
"       }\n"
"\n"
"QPushButton {\n"
"       min-width:100px;\n"
"       min-height:40px;\n"
"       border-radius:10px;\n"
"       }\n"
"\n"
"QScrollBar:horizontal {\n"
"       border: 1px solid #222222;\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #ffffff, stop: 0.5 #ffffff, stop: 1 #ffffff);\n"
"       heig"
                        "ht: 7px;\n"
"       margin: 0px 16px 0 16px;\n"
"       }\n"
"QScrollBar::handle:horizontal {\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #b1b1b1, stop: 0.5 #b3b3b3, stop: 1 #b1b1b1);\n"
"       min-height: 20px;\n"
"       border-radius: 20px;\n"
"       }\n"
"QScrollBar::add-line:horizontal {\n"
"       border: 1px solid #1b1b19;\n"
"       border-radius: 20px;\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #999999, stop: 1 #999999);\n"
"       width: 14px;\n"
"       subcontrol-position: right;\n"
"       subcontrol-origin: margin;\n"
"       }\n"
"QScrollBar::sub-line:horizontal {\n"
"       border: 1px solid #1b1b19;\n"
"       border-radius: 20px;\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #999999, stop: 1 #999999);\n"
"       width: 14px;\n"
"       subcontrol-position: left;\n"
"       subcontrol-origin: margin;\n"
"       }\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal {\n"
"      "
                        " border: 1px solid black;\n"
"       width: 1px;\n"
"       height: 1px;\n"
"       background: white;\n"
"       }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"       background: none;\n"
"       }\n"
"QScrollBar:vertical {\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #ffffff, stop: 0.5 #ffffff, stop: 1 #ffffff);\n"
"       width: 7px;\n"
"       margin: 16px 0 16px 0;\n"
"       border: 1px solid #222222;\n"
"       }\n"
"QScrollBar::handle:vertical {\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b1b1b1, stop: 0.5 #b3b3b3, stop: 1 #b1b1b1);\n"
"       min-height: 20px;\n"
"       border-radius: 20px;\n"
"       }\n"
"QScrollBar::add-line:vertical {\n"
"       border: 1px solid #1b1b19;\n"
"       border-radius: 20px;\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #999999, stop: 1 #999999);\n"
"       height: 14px;\n"
"       subcontrol-position: bottom;\n"
"       subcontrol-origin: marg"
                        "in;\n"
"       }\n"
"QScrollBar::sub-line:vertical {\n"
"       border: 1px solid #1b1b19;\n"
"       border-radius: 20px;\n"
"       background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #999999, stop: 1 #999999);\n"
"       height: 14px;\n"
"       subcontrol-position: top;\n"
"       subcontrol-origin: margin;\n"
"       }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"       border: 1px solid black;\n"
"       width: 1px;\n"
"       height: 1px;\n"
"       background: white;\n"
"       }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"       background: none;\n"
"       }\n"
"\n"
"QTabWidget::pane {\n"
"       border: 1px solid #444;\n"
"       top: 1px;\n"
"       }\n"
"\n"
"QTabBar::tab {\n"
"       color: #ffffff;\n"
"       border: 1px solid #444;\n"
"       border-bottom-style: none;\n"
"       background-color: #999999;\n"
"       padding-left: 10px;\n"
"       padding-right: 10px;\n"
"       padding-top: 3px;\n"
"       padding-bottom: 2px;"
                        "\n"
"       margin-right: -1px;\n"
"       min-width: 80px;\n"
"       min-height: 30px;\n"
"       }\n"
"QTabBar::tab:last {\n"
"       margin-right: 0;\n"
"       border-top-right-radius: 3px;\n"
"       }\n"
"QTabBar::tab:first:!selected {\n"
"       margin-left: 0px;\n"
"       border-top-left-radius: 3px;\n"
"       }\n"
"QTabBar::tab:!selected {\n"
"       border-bottom-style: solid;\n"
"       margin-top: 3px;\n"
"       background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #1874CD, stop:.4 #737373);\n"
"       }\n"
"QTabBar::tab:selected {\n"
"       border-top-left-radius: 3px;\n"
"       border-top-right-radius: 3px;\n"
"       margin-bottom: 0px;\n"
"       }\n"
"QTabBar::tab:!selected:hover  {\n"
"       border-top-left-radius: 3px;\n"
"       border-top-right-radius: 3px;\n"
"       background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #737373, stop:0.2 #999999, stop:0.1 #b1b1b1);\n"
"       }\n"
"\n"
"   ")
        self.openAct = QAction(MainUi)
        self.openAct.setObjectName(u"openAct")
        self.saveAct = QAction(MainUi)
        self.saveAct.setObjectName(u"saveAct")
        self.saveAct.setCheckable(False)
        self.saveAct.setEnabled(True)
        self.exitAct = QAction(MainUi)
        self.exitAct.setObjectName(u"exitAct")
        self.openFilePathAct = QAction(MainUi)
        self.openFilePathAct.setObjectName(u"openFilePathAct")
        self.saveFilePathAct = QAction(MainUi)
        self.saveFilePathAct.setObjectName(u"saveFilePathAct")
        self.thresholdAct = QAction(MainUi)
        self.thresholdAct.setObjectName(u"thresholdAct")
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
        self.openImageFileScrollWidget.setGeometry(QRect(0, 0, 936, 872))
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
        self.tabInnerWidget1.setGeometry(QRect(0, 0, 896, 857))
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
        self.tabInnerWidget2.setGeometry(QRect(0, 0, 51, 40))
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
        self.tabInnerWidget3.setGeometry(QRect(0, 0, 51, 40))
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
        self.tabInnerWidget4.setGeometry(QRect(0, 0, 51, 40))
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
        self.tabInnerWidget5.setGeometry(QRect(0, 0, 51, 40))
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
        self.menuBar.setGeometry(QRect(0, 0, 1920, 35))
        self.fileMenu = QMenu(self.menuBar)
        self.fileMenu.setObjectName(u"fileMenu")
        self.opencvMenu = QMenu(self.menuBar)
        self.opencvMenu.setObjectName(u"opencvMenu")
        self.image = QMenu(self.opencvMenu)
        self.image.setObjectName(u"image")
        MainUi.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainUi)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainUi.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainUi)
        self.statusBar.setObjectName(u"statusBar")
        MainUi.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.opencvMenu.menuAction())
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.openFilePathAct)
        self.fileMenu.addAction(self.saveFilePathAct)
        self.fileMenu.addAction(self.exitAct)
        self.opencvMenu.addAction(self.image.menuAction())
        self.image.addAction(self.thresholdAct)

        self.retranslateUi(MainUi)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainUi)
    # setupUi

    def retranslateUi(self, MainUi):
        MainUi.setWindowTitle(QCoreApplication.translate("MainUi", u"ImageOperationModel", None))
        self.openAct.setText(QCoreApplication.translate("MainUi", u"\u6253\u5f00\u56fe\u7247", None))
#if QT_CONFIG(shortcut)
        self.openAct.setShortcut(QCoreApplication.translate("MainUi", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.saveAct.setText(QCoreApplication.translate("MainUi", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.saveAct.setShortcut(QCoreApplication.translate("MainUi", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.exitAct.setText(QCoreApplication.translate("MainUi", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.exitAct.setShortcut(QCoreApplication.translate("MainUi", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.openFilePathAct.setText(QCoreApplication.translate("MainUi", u"\u8bbe\u7f6e\u8bfb\u53d6\u6587\u4ef6\u5939", None))
        self.saveFilePathAct.setText(QCoreApplication.translate("MainUi", u"\u8bbe\u7f6e\u4fdd\u5b58\u6587\u4ef6\u5939", None))
        self.thresholdAct.setText(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u9608\u503c", None))
        self.thresholdAct.setIconText(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u9608\u503c", None))
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
        self.fileMenu.setTitle(QCoreApplication.translate("MainUi", u"\u6587\u4ef6", None))
        self.opencvMenu.setTitle(QCoreApplication.translate("MainUi", u"OpenCV", None))
        self.image.setTitle(QCoreApplication.translate("MainUi", u"\u56fe\u50cf\u5904\u7406", None))
    # retranslateUi

