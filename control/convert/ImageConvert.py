import cv2
from PySide6.QtGui import QImage, QPixmap


def cImage2QPixmap(cImage):
    # 大小
    height, width, depth = cImage.shape
    # 转换格式
    cImage = cv2.cvtColor(cImage, cv2.COLOR_BGR2RGB)
    # 转换为QImage
    qImage = QImage(cImage.data, width, height, width * depth, QImage.Format_RGB888)
    # 转换为QPixmap
    qPixmap = QPixmap.fromImage(qImage)
    # 返回结果
    return qPixmap
