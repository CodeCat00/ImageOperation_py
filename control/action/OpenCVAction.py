from PySide6.QtWidgets import QLabel

from control.convert.ImageConvert import cImage2QPixmap
from control.image.OpenCVManager import threshold, blur, medianBlur, bilateralFilter, dilate, \
    morphologyExOpen, morphologyExClose, morphologyExGradient, morphologyExTophat, morphologyExBlackhat, \
    findContours, equalizeHist, createCLAHE, watershed, grabCut, \
    gaussianBlur, houghCircles, houghLinesP, houghLines, sobel, canny
from model.ImageOperationmodel import ImageOperationModel


def updateImageInfo(image, model=ImageOperationModel, label=QLabel):
    # 更新处理结果
    model.getImageModel().setDealImage(image)
    # 显示图片
    label.setPixmap(cImage2QPixmap(model.getImageModel().showImage))


def thresholdAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = threshold(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def blurAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = blur(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def gaussianBlurAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = gaussianBlur(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def medianBlurAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = medianBlur(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def bilateralFilterAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = bilateralFilter(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def morphologyExOpenAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = morphologyExOpen(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def morphologyExCloseAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = morphologyExClose(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def morphologyExGradientAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = morphologyExGradient(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def morphologyExTophatAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = morphologyExTophat(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def morphologyExBlackhatAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = morphologyExBlackhat(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def sobelAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = sobel(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def cannyAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = canny(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def dilateAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = dilate(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def findContoursAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = findContours(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def equalizeHistAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = equalizeHist(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def createCLAHEAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = createCLAHE(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def houghLinesAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = houghLines(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def houghLinesPAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = houghLinesP(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def houghCirclesAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = houghCircles(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def watershedAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = watershed(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)


def grabCutAct(model=ImageOperationModel, label=QLabel):
    # 灰度处理
    image = grabCut(model.getImageModel().inImage)
    # 更新图片相关信息
    updateImageInfo(image, model, label)
