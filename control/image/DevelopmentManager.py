import cv2
import numpy as np


def test(image):
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 计算图像的傅里叶变换
    f_transform = np.fft.fft2(gray)
    f_shift = np.fft.fftshift(f_transform)
    # 取幅值并对数变换以增强对比
    magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)
    # 找到图像的主频
    rows, cols = gray.shape
    crow, ccol = rows // 2, cols // 2  # 图像中心
    magnitude_spectrum[crow - 10:crow + 10, ccol - 10:ccol + 10] = 0  # 屏蔽低频区域
    # 找到频谱中的峰值（主频对应的点）
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(magnitude_spectrum)
    # 计算重复单元的周期
    period_x = abs(ccol - max_loc[0])
    period_y = abs(crow - max_loc[1])
    # 裁剪最小重复单元
    unit = image[0:period_y, 0:period_x]
    return unit
