import cv2


# 图像灰度处理
def gray(img):
    # 灰度处理
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 返回结果
    return img_gray
