import cv2


# 调整图像大小
def resizeImage(image, minWidth, maxWidth, defaultWidth):
    # 获取图像大小
    height, width, _ = shape(image)
    # 比较边界
    if minWidth < width < maxWidth:
        return image
    # 重新设置大小
    defaultHeight = int(height / width * defaultWidth)
    image = cv2.resize(image, (defaultWidth, defaultHeight))
    # 返回结果
    return image


# 获取图片通道
def shape(image):
    return image.shape if len(image.shape) == 3 else (*image.shape, 1)
