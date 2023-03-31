# 临时附加的功能：导出一个视频

import pixelMaker_Basic
import imgMaker
import cv2

# 默认的函数选择策略
def defaultStrategy(funcList:list, frameId:int):
    return funcList[frameId % len(funcList)]

# 随机的函数选择策略
def randomStrategy(funcList:list, frameId:int):
    import random
    return funcList[random.randint(0, len(funcList)-1)]

defaultFunc={
    "function" : pixelMaker_Basic.randPixel,
    "para" : {}
}

# 构造一个特殊的视频片段
# path          视频的存储路径
# frameNumber   视频的总帧数
# size          帧尺寸（二元元组）
# fps           视频的帧率
# strategy      帧生成策略
#                   这个函数具有两个参数
#                       funcList    策略使用的函数和参数列表
#                       frameId     帧序号
#                   这个函数返回一个字典
#                       "function"  本帧使用的像素构造函数
#                       "para"      像素构造函数的参数表（字典）
# funcList      策略使用的函数及其参数列表
#                   要求与帧生成策略函数匹配
# showInfo      是否展示生成进度
def videoMaker(path:str, frameNumber:int, size:tuple = (960, 540), fps:int = 12, strategy = defaultStrategy, funcList = [defaultFunc], showInfo:bool = False):
    video=cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*"mp4v"), fps, size)
    for i in range(frameNumber):
        func=strategy(funcList, i)
        if showInfo==True:
            print("正在绘制第 ", i, " 帧")
        video.write(imgMaker.imgMaker(size[0], size[1], True, func["function"], func["para"]))
    video.release()

if __name__=="__main__":
    funcList=[]
    import math
    import numpy
    import random

    def func1(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32):
        return 0.33*(math.sin(y/w*10*math.pi)+1)+0.33
    def func2(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32):
        return y/w
    def func3(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32):
        return x/h
    def func4(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32):
        return 0.33*(math.sin(y/w*2*math.pi)+1)+0.33
    def func5(w:numpy.uint32, h:numpy.uint32, x:numpy.uint32, y:numpy.uint32):
        return random.random()*0.5+0.25

    funcList.append({
        "function" : pixelMaker_Basic.inhomogeneousPixel,
        "para" : {"func" : func1}
    })
    funcList.append({
        "function" : pixelMaker_Basic.inhomogeneousPixel,
        "para" : {"func" : func2}
    })
    funcList.append({
        "function" : pixelMaker_Basic.inhomogeneousPixel,
        "para" : {"func" : func3}
    })
    funcList.append({
        "function" : pixelMaker_Basic.inhomogeneousPixel,
        "para" : {"func" : func4}
    })
    funcList.append({
        "function" : pixelMaker_Basic.inhomogeneousPixel,
        "para" : {"func" : func5}
    })
    for d in funcList:
        d["para"]["color"]=(32, 32, 32)
        d["para"]["backColor"]=(0, 0, 0)
    
    videoMaker("res3.mp4", 240, strategy=randomStrategy, funcList=funcList, showInfo=True)