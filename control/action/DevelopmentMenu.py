from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.DevelopmentManager import test
from model.ImageOperationModel import ImageOperationModel


# canny边缘检测
def testAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(test, model, label)
