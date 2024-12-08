import cv2
import numpy as np


# Laplacian微分
def laplacian(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Laplacian微分
    lap = cv2.Laplacian(image, cv2.CV_64F)
    res = np.uint8(lap)
    # 返回结果
    return res


# sobelX
def sobelX(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # sobelX
    sobel = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    res = np.uint8(sobel)
    # 返回结果
    return res


# sobelY
def sobelY(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # sobelY
    sobel = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    res = np.uint8(sobel)
    # 返回结果
    return res