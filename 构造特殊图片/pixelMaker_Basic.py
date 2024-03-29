import numpy
import random

def uint8rand():
    return numpy.uint8(random.randint(0, 255))

# 生成随机噪音
# 不需要额外参数
def randPixel(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32, isColored:bool, para:dict):
    if isColored==False:
        return uint8rand()
    else:
        return numpy.array((uint8rand(), uint8rand(), uint8rand()))

# 生成纵向单色条纹
# 额外参数：
#   color       条纹颜色
#   gapColor    间隔颜色
#   size        条纹宽度
#   gapSize     条纹间距
def stripeCol(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32, isColored:bool, para:dict):
    if y % (para["size"]+para["gapSize"])>=para["size"]:
        return para["gapColor"]
    else:
        return para["color"]
    
# 生成横向单色条纹
# 额外参数：
#   color       条纹颜色
#   gapColor    间隔颜色
#   size        条纹宽度
#   gapSize     条纹间距
def stripeRow(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32, isColored:bool, para:dict):
    if x % (para["size"]+para["gapSize"])>=para["size"]:
        return para["gapColor"]
    else:
        return para["color"]
    
# 生成正交网格（垂直于轴）
# 额外参数：
#   color           网格线颜色
#   spaceColor      空格颜色
#   rowSize         横向网格线宽度
#   colSize         纵向网格线宽度
#   spaceWidth      空格尺寸(横向)
#   spaceHeight     空格尺寸(纵向)
def gridXY(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32, isColored:bool, para:dict):
    if y % (para["colSize"]+para["spaceWidth"])>=para["colSize"] and x % (para["rowSize"]+para["spaceHeight"])>=para["rowSize"]:
        return para["spaceColor"]
    else:
        return para["color"]

# 构造不均匀单色噪声
# 额外参数：
#   func        噪音分布
#                   接受四个参数, w, h, x, y
#                   返回一个[0, 1]浮点数，表示这一点出现噪音的概率
#   color       噪音颜色
#   backColor   背景颜色
def inhomogeneousPixel(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32, isColored:bool, para:dict):
    func=para["func"]
    if random.random()<=func(w, h, x, y):
        return para["color"]
    else:
        return para["backColor"]
    
# 构造不均匀随机噪声
# 额外参数：
#   func        噪音分布
#                   接受四个参数, w, h, x, y
#                   返回一个[0, 1]浮点数，表示这一点出现噪音的概率
#   backColor   背景颜色
def inhomogeneousRandomPixel(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32, isColored:bool, para:dict):
    func=para["func"]
    if random.random()<=func(w, h, x, y):
        return uint8rand()
    else:
        return para["backColor"]