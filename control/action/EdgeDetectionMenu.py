from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.EdgeDetectionManager import *
from model.ImageOperationModel import ImageOperationModel


# canny边缘检测
def cannyAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(canny, model, label)
