import cv2
import numpy as np

from control.image.ImageBasicManager import shape


# 缩放
def resize(image):
    # 缩放
    res = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # 返回结果
    return res


# 平移
def translation(image):
    # 读取通道
    rows, cols, _ = shape(image)
    # 平移
    m = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(image, m, (cols, rows))
    # 返回结果
    return dst


# 旋转
def rotation(image):
    # 读取通道
    rows, cols, _ = shape(image)
    # 旋转
    m = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
    dst = cv2.warpAffine(image, m, (cols, rows))
    # 返回结果
    return dst


# 仿射变换
def warpAffine(image):
    # 读取通道
    rows, cols, ch = shape(image)
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    # 仿射变换
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(image, M, (cols, rows))
    # 返回结果
    return dst


# 透视变换
def warpPerspective(image):
    # 读取通道
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    # 透视变换
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(image, M, (300, 300))
    # 返回结果
    return dst
