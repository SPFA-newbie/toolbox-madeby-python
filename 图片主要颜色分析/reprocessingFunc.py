# 将原始结果处理成倒排表
# originalDict  将要处理的结果字典
# filter        过滤器, 用于过滤一些值
#                   具有两个参数
#                       - color     当前项的颜色
#                       - value     当前项颜色的计数值
#                   返回一个布尔结果，True代表项通过, False代表项未通过过滤
def inversionCountDict(originalDict:dict, filter=lambda color, value:True):
    inversionDict={}
    for color,value in originalDict.items():
        if filter(color, value)==True:
            if value not in inversionDict:
                inversionDict[value]=[]
            inversionDict[value].append(color)
    return inversionDict

# 对原始结果进行默认排序（降序）
def defaultSortOriginalDict(originalDict:dict):
    result=sorted(originalDict.items(), key=lambda item:item[1], reverse=True)
    return result

# 用最多的四种颜色构建一张图片
def makeMainColorImg(colorList:list):
    import numpy
    result=numpy.zeros((100, 400, 3), dtype=numpy.uint8)
    while len(colorList)<4:
        colorList.append((0, 0, 0))
    for x in range(100):
        for y in range(400):
            result[x, y, 0]=numpy.uint8(colorList[y//100][0][0])
            result[x, y, 1]=numpy.uint8(colorList[y//100][0][1])
            result[x, y, 2]=numpy.uint8(colorList[y//100][0][2])
    return result