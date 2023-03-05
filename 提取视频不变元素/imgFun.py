import cv2 as cv

# 默认的高斯卷积函数
def defaultGaussianBlur(img):
    return cv.GaussianBlur(img, (3, 3), 1)

# 像素比较
# point1,2      要比较的两个点
# maxD          容差
def pixelCompare(point1, point2, maxD=(32, 32, 32)):
    if abs(int(point1[0])-int(point2[0]))>maxD[0]:return False
    if abs(int(point1[1])-int(point2[1]))>maxD[1]:return False
    if abs(int(point1[2])-int(point2[2]))>maxD[2]:return False
    return True

# img1,2        要比较的两个图片
# replace       使用什么像素替换不同的部分
# maxD          像素的最大容差
# blur          图片的处理方法（默认高斯卷积）
def findSamePixel(img1, img2, replace=(0, 255, 0), maxD=(32, 32, 32), blur=defaultGaussianBlur):
    if blur!=None:
        result=blur(img1)
        p2=blur(img2)
    else:
        result=img1
        p2=img2
    
    (row, col, nouse)=result.shape
    for x in range(row):
        for y in range(col):
            if pixelCompare(result[x, y], p2[x, y], maxD)==False:
                result[x,y]=replace
    return result

if __name__=="__main__":
    img1=cv.imread("test1.jpg")
    img2=cv.imread("test2.jpg")
    result=findSamePixel(img1=img1, img2=img2)
    cv.imwrite("Test_result.jpg", result)
    