from PySide6.QtWidgets import QLabel

from control.action.CommonAction import menuActionTemplate
from control.image.GradientManager import *
from model.ImageOperationModel import ImageOperationModel


# Laplacian微分
def laplacianAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(laplacian, model, label)


# sobelX
def sobelXAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(sobelX, model, label)


# sobelY
def sobelYAct(model=ImageOperationModel, label=QLabel):
    menuActionTemplate(sobelY, model, label)
