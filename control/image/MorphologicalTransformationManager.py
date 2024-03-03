import cv2
import numpy as np


# 腐蚀
def erosion(img):
    # 腐蚀
    res = cv2.blur(img, (5, 5))
    # 返回结果
    return res


# 膨胀
def dilate(img):
    # 卷积核
    kernel = np.ones((5, 5), np.float32) / 25
    # 膨胀
    res = cv2.dilate(img, kernel, iterations=1)
    # 返回结果
    return res


# 开运算
def morphologyExOpen(img):
    # 卷积核
    kernel = np.ones((5, 5), np.float32) / 25
    # 开运算
    res = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # 返回结果
    return res


# 闭运算
def morphologyExClose(img):
    # 卷积核
    kernel = np.ones((5, 5), np.float32) / 25
    # 闭运算
    res = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    # 返回结果
    return res


# 形态梯度
def morphologyExGradient(img):
    # 卷积核
    kernel = np.ones((5, 5), np.float32) / 25
    # 形态梯度
    res = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    # 返回结果
    return res


# 顶帽
def morphologyExTopHat(img):
    # 卷积核
    kernel = np.ones((5, 5), np.float32) / 25
    # 顶帽
    res = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    # 返回结果
    return res


# 黑帽
def morphologyExBlackHat(img):
    # 卷积核
    kernel = np.ones((5, 5), np.float32) / 25
    # 黑帽
    res = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    # 返回结果
    return res
