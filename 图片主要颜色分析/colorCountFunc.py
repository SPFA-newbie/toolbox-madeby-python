import numpy as np

# 将相近颜色归一化
def singleChannelDiff(pixel:np.ndarray, diff:np.uint8 = 16):
    (b, g, r)=tuple(pixel)
    if b % diff < diff // 2: b = b // diff * diff
    else: b = b // diff * diff + diff

    if g % diff < diff // 2:  g = g // diff * diff
    else: g = g // diff * diff + diff

    if r % diff < diff // 2: r = r // diff * diff
    else: r = r // diff * diff + diff
    
    if b > 255: b = 255
    if g > 255: g = 255
    if r > 255: r = 255
    return [(b, g, r)]

# 临时函数
def testFun(pixel, para):
    return singleChannelDiff(pixel, 64)