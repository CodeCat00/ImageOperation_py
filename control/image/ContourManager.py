import cv2


# 轮廓近似
def approxPolyDP(image):
    # 复制
    gray = image
    # 转灰度
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行边缘检测
    edges = cv2.Canny(gray, 50, 150)
    # 查找轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 循环遍历每个轮廓
    for contour in contours:
        # 计算轮廓周长
        epsilon = 0.1 * cv2.arcLength(contour, True)
        # 近似轮廓
        approx = cv2.approxPolyDP(contour, epsilon, True)
        # 绘制近似的多边形
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    # 返回结果
    return image


# 凸包
def convexHull(image):
    # 复制
    gray = image
    # 转灰度
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行边缘检测
    edges = cv2.Canny(gray, 50, 150)
    # 查找轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 循环遍历每个轮廓
    for contour in contours:
        # 获取凸包
        hull = cv2.convexHull(contour)
        # 绘制凸包
        cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
    # 返回结果
    return image


# 旋转矩形
def drawContours(image):
    # 复制
    gray = image
    # 转灰度
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行边缘检测
    edges = cv2.Canny(gray, 50, 150)
    # 查找轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 在图像上绘制轮廓
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    # 返回结果
    return image


# 最小外圆
def circle(image):
    # 复制
    gray = image
    # 转灰度
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行边缘检测
    edges = cv2.Canny(gray, 50, 150)
    # 查找轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 遍历每个轮廓
    for contour in contours:
        # 计算最小外接圆
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        # 在图像上绘制最小外接圆
        cv2.circle(image, center, radius, (0, 255, 0), 2)
    # 返回结果
    return image


# 拟合椭圆
def ellipse(image):
    # 复制
    gray = image
    # 转灰度
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行边缘检测
    edges = cv2.Canny(gray, 50, 150)
    # 查找轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 遍历每个轮廓
    for contour in contours:
        # 检查轮廓点数是否足够
        if len(contour) >= 5:
            # 拟合椭圆
            ellipse = cv2.fitEllipse(contour)
            # 在图像上绘制椭圆
            cv2.ellipse(image, ellipse, (0, 255, 0), 2)
    # 返回结果
    return image


# 拟合线
def line(image):
    # 复制
    gray = image
    # 转灰度
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行边缘检测
    edges = cv2.Canny(gray, 50, 150)
    # 查找轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 遍历每个轮廓
    for contour in contours:
        # 拟合直线
        [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
        # 获取直线的斜率和截距
        slope = vy / vx
        intercept = y - (slope * x)
        # 计算直线上的两个点
        x1 = int(x - 1000 * vx)
        y1 = int(y - 1000 * vy)
        x2 = int(x + 1000 * vx)
        y2 = int(y + 1000 * vy)
        # 在图像上绘制直线
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # 返回结果
    return image
