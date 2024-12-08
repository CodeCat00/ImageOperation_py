# Canny边缘检测
import cv2
import numpy as np


def canny(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Canny边缘检测
    sobel = cv2.Canny(image, 100, 200)
    res = np.uint8(sobel)
    # 返回结果
    return res
