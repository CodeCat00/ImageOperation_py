# Canny边缘检测
import cv2
import numpy as np


def canny(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Canny边缘检测
    sobel = cv2.Canny(img, 100, 200)
    res = np.uint8(sobel)
    # 返回结果
    return res
