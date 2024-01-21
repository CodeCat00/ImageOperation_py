import cv2
from PySide6.QtGui import QImage, QPixmap


# 图片格式转换 mat -> QImage
def cImageToQImage(cImage):
    # 灰度图
    if len(cImage.shape) == 2:
        cImage = cv2.cvtColor(cImage, cv2.COLOR_GRAY2RGB)
    # 转换
    height, width, channel = cImage.shape
    bytesPerLine = channel * width
    qimage = QImage(cImage.data, width, height, bytesPerLine, QImage.Format_RGB888)
    # 返回结果
    return qimage.copy()


# 图片格式转换 mat -> QPixmap
def cImageToQPixmap(cImage):
    # 大小
    height, width, depth = cImage.shape if len(cImage.shape) == 3 else (*cImage.shape, 1)
    # 转换格式
    cImage = cv2.cvtColor(cImage, cv2.COLOR_BGR2RGB)
    # 转换为QImage
    qImage = cImageToQImage(cImage)
    # 转换为QPixmap
    qPixmap = QPixmap.fromImage(qImage)
    # 返回结果
    return qPixmap
