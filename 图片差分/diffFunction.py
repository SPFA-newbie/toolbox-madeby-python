import cv2
import numpy

# pixel1, pixel2    进行减法的像素
# 小于0的差归为0
def defSub(pixel1, pixel2):
    ret=pixel1
    for i in range(ret.shape[0]):
        val=int(pixel1[i])-int(pixel2[i])
        if val<0: val=0
        ret[i]=numpy.uint8(val)
    return ret

# 使用差的绝对值
def absSub(pixel1, pixel2):
    ret=pixel1
    for i in range(ret.shape[0]):
        val=int(pixel1[i])-int(pixel2[i])
        if val<0: val=-val
        ret[i]=numpy.uint8(val)
    return ret

# 将差除2后加128
def halfSub(pixel1, pixel2):
    ret=pixel1
    for i in range(ret.shape[0]):
        val=int(pixel1[i])-int(pixel2[i])
        val/=2
        val+=128
        ret[i]=numpy.uint8(val)
    return ret


# 求图片的差分
# img1, img2    进行差分的图片
def diffImg(img1, img2, subFunction=defSub):
    if img1.shape != img2.shape:
        raise Exception("图像不匹配, img1="+img1.shape+", img2="+img2.shape)
    ret=img1
    (row, col, nouse)=img1.shape
    for x in range(row):
        for y in range(col):
            ret[x, y]=subFunction(img1[x, y], img2[x, y])
    return ret


if __name__=="__main__":
    img1=cv2.imread("test1.jpg")
    img2=cv2.imread("test2.jpg")
    cv2.imwrite("result.jpg", diffImg(img1, img2, defSub))