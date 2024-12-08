import cv2


# 简单二值化阈值
def simpleBinaryThreshold(image):
    # 简单二值化阈值
    _, res = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # 返回结果
    return res


# 简单反二值化阈值
def simpleBinaryInvThreshold(image):
    # 简单反二值化阈值
    _, res = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    # 返回结果
    return res


# 简单截断阈值
def simpleTruncThreshold(image):
    # 简单截断阈值
    _, res = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
    # 返回结果
    return res


# 简单置零阈值
def simpleToZeroThreshold(image):
    # 简单置零阈值
    _, res = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
    # 返回结果
    return res


# 简单置零反阈值
def simpleToZeroInvThreshold(image):
    # 简单置零反阈值
    _, res = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
    # 返回结果
    return res


# 自适应均值阈值
def adaptiveMeanThreshold(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 中值滤波
    image = cv2.medianBlur(image, 5)
    # 自适应均值阈值
    res = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # 返回结果
    return res


# 自适应高斯阈值
def adaptiveGaussianThreshold(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 中值滤波
    image = cv2.medianBlur(image, 5)
    # 自适应高斯阈值
    res = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # 返回结果
    return res


# OTSU二值化
def OTSUThreshold(image):
    # 转灰度
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # OTSU二值化
    _, res = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 返回结果
    return res
