import cv2


# 图像灰度
def gray(img):
    # 灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 返回结果
    return img_gray


# 图像反转
def flip(img):
    # 反转
    flipped_both = cv2.flip(img, -1)
    # 返回结果
    return flipped_both
