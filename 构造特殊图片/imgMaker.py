import cv2
import numpy
import pixelMaker_Basic as pMaker

# 构造一个特殊的图片
# w, h              图片尺寸
# isColored         是否为彩色图片
# pixelMaker        像素构造函数
#                       这个函数应当拥有六个参数
#                           - w, h      图片尺寸
#                           - x, y      将要构造的像素的位置
#                           - isColored 是否为彩色
#                           - para      其他参数构成的列表
# pixelMakerPara   构造函数的其他参数
def imgMaker(w:numpy.uint32, h:numpy.uint32, isColored:bool = True, pixelMaker = pMaker.randPixel, pixelMakerPara:dict = {}):
    if isColored==True:
        img=numpy.zeros((h, w, 3), numpy.uint8)
    else:
        img=numpy.zeros((h, w), numpy.uint8)
    
    for x in range(h):
        for y in range(w):
            img[x,y]=pixelMaker(w, h, x, y, isColored, pixelMakerPara)
    
    return img

if __name__=="__main__":
    gridPara={}
    gridPara["color"]=numpy.array((255, 255, 255), dtype=numpy.uint8)
    gridPara["spaceColor"]=numpy.array((0, 0, 0), dtype=numpy.uint8)
    gridPara["spaceWidth"]=10
    gridPara["spaceHeight"]=1
    gridPara["rowSize"]=1
    gridPara["colSize"]=10

    img=imgMaker(900, 600, True, pMaker.gridXY, gridPara)
    cv2.imwrite("result.jpg", img)