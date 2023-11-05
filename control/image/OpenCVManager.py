import cv2
import numpy as np


def threshold(img):
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return thresh


def blur(img):
    return cv2.blur(img, (5, 5))


def gaussianBlur(img):
    return cv2.GaussianBlur(img, (5, 5), 0)


def medianBlur(img):
    return cv2.medianBlur(img, 5)


def bilateralFilter(img):
    return cv2.bilateralFilter(img, 9, 75, 75)


def dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)


def morphologyEx(img, type):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, type, kernel)


def morphologyExOpen(img):
    return morphologyEx(img, cv2.MORPH_OPEN)


def morphologyExClose(img):
    return morphologyEx(img, cv2.MORPH_CLOSE)


def morphologyExGradient(img):
    return morphologyEx(img, cv2.MORPH_GRADIENT)


def morphologyExTophat(img):
    return morphologyEx(img, cv2.MORPH_TOPHAT)


def morphologyExBlackhat(img):
    return morphologyEx(img, cv2.MORPH_BLACKHAT)


def sobel(img):
    return cv2.Laplacian(img, cv2.CV_64F)


def canny(img):
    return cv2.Canny(img, 100, 200)


def findContours(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    cnt = contours[0]
    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.line(img, start, end, [0, 255, 0], 2)
        cv2.circle(img, far, 5, [0, 0, 255], -1)
    return img


def equalizeHist(img):
    equ = cv2.equalizeHist(img)
    return np.hstack((img, equ))


def createCLAHE(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(img)


def houghLines(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return img


def houghLinesP(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return img


def houghCircles(img):
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    return img


def watershed(img):
    # 转换格式
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret0, thresh0 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # 开操作
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh0, cv2.MORPH_OPEN, kernel, iterations=2)
    # 确定背景区域
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    # 确定前景区域
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret1, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    # 查找未知区域
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    # 标记标签
    ret2, markers1 = cv2.connectedComponents(sure_fg)
    markers = markers1 + 1
    markers[unknown == 255] = 0
    markers3 = cv2.watershed(img, markers)
    img[markers3 == -1] = [0, 255, 0]
    # 返回结果
    return img


def grabCut(img):
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (50, 50, 450, 290)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    return img * mask2[:, :, np.newaxis]
