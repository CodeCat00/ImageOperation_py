import cv2
import numpy as np


# Laplacian微分
def laplacian(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Laplacian微分
    lap = cv2.Laplacian(img, cv2.CV_64F)
    res = np.uint8(lap)
    # 返回结果
    return res


# sobelX
def sobelX(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # sobelX
    sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    res = np.uint8(sobel)
    # 返回结果
    return res


# sobelY
def sobelY(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # sobelY
    sobel = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    res = np.uint8(sobel)
    # 返回结果
    return res