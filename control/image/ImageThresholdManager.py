import cv2


# 简单二值化阈值
def simpleBinaryThreshold(img):
    # 简单二值化阈值
    _, res = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # 返回结果
    return res


# 简单反二值化阈值
def simpleBinaryInvThreshold(img):
    # 简单反二值化阈值
    _, res = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # 返回结果
    return res


# 简单截断阈值
def simpleTruncThreshold(img):
    # 简单截断阈值
    _, res = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    # 返回结果
    return res


# 简单置零阈值
def simpleToZeroThreshold(img):
    # 简单置零阈值
    _, res = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    # 返回结果
    return res


# 简单置零反阈值
def simpleToZeroInvThreshold(img):
    # 简单置零反阈值
    _, res = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    # 返回结果
    return res


# 自适应均值阈值
def adaptiveMeanThreshold(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 中值滤波
    img = cv2.medianBlur(img, 5)
    # 自适应均值阈值
    res = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # 返回结果
    return res


# 自适应高斯阈值
def adaptiveGaussianThreshold(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 中值滤波
    img = cv2.medianBlur(img, 5)
    # 自适应高斯阈值
    res = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # 返回结果
    return res


# OTSU二值化
def OTSUThreshold(img):
    # 转灰度
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # OTSU二值化
    _, res = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 返回结果
    return res
