import cv2
import numpy as np


# 二维卷积
def filter2D(image):
    # 二维卷积
    kernel = np.ones((5, 5), np.float32) / 25
    res = cv2.filter2D(image, -1, kernel)
    # 返回结果
    return res


# 均值模糊
def blur(image):
    # 均值模糊
    res = cv2.blur(image, (5, 5))
    # 返回结果
    return res


# 高斯模糊
def gaussianBlur(image):
    # 高斯模糊
    res = cv2.GaussianBlur(image, (5, 5), 0)
    # 返回结果
    return res


# 中值滤波
def medianBlur(image):
    # 中值滤波
    res = cv2.medianBlur(image, 5)
    # 返回结果
    return res


# 双边滤波
def bilateralFilter(image):
    # 双边滤波
    res = cv2.bilateralFilter(image, 9, 75, 75)
    # 返回结果
    return res
