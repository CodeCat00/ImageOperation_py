import cv2


def resizeImage(image, minWidth, maxWidth, defaultWidth):
    # 获取图像大小
    height, width, _ = image.shape
    # 比较边界
    if minWidth < width < maxWidth:
        return image
    # 重新设置大小
    defaultHeight = int(height / width * defaultWidth)
    image = cv2.resize(image, (defaultWidth, defaultHeight))
    # 返回结果
    return image


def threshold(image):
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return thresh