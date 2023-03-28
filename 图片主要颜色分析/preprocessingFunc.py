# 默认的高斯卷积函数
def defaultGaussianBlur(img):
    import cv2
    return cv2.GaussianBlur(img, (3, 3), 1)