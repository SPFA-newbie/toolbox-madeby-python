import numpy as np

# 默认的颜色计数方式, 不进行任何处理
def originalPixelCount(pixel:np.ndarray, para:dict):
    return [tuple(pixel)]

# 对图像中的颜色进行计数, 默认后处理条件下返回一个字典
# img               将要进行处理的图像
# countFunction     颜色计数的方式
#                       函数需要接受两个参数
#                           - pixel     当前的像素
#                           - para      函数的参数表（字典）
#                       函数返回一个列表, 记录获取的颜色
# funPara           颜色计数函数的参数表（字典）
# preprocessing     对图像进行预处理的函数串（列表）
#                       函数接受图像img作为参数, 同时返回一个处理后的图像
# reprocessing      对结果进行后处理的函数串（列表）
#                       函数串的第一个函数将字典result作为参数
#                           - result的结构为：{tuple:int}, tuple是一个表示颜色的元组, int表示颜色的计数
def colorAnalyse(img:np.ndarray, countFunction = originalPixelCount, funPara:dict = {}, preprocessing:list = [], reprocessing:list = []):
    for func in preprocessing:
        img=func(img)
    
    (row, col, nouse)=img.shape
    result={}
    for x in range(row):
        for y in range(col):
            pRes=countFunction(img[x][y], funPara)
            for r in pRes:
                if r in result:
                    result[r]+=1
                else:
                    result[r]=1
    
    for func in reprocessing:
        result=func(result)
    return result

if __name__=="__main__":
    import cv2
    import colorCountFunc as cntf
    import reprocessingFunc as ref
    import preprocessingFunc as pref
    img=cv2.imread("test.jpg")
    img=cv2.resize(img, (480, 270), interpolation=cv2.INTER_CUBIC)

    # res=colorAnalyse(img, countFunction=cntf.testFun, preprocessing=[pref.defaultGaussianBlur], reprocessing=[ref.defaultSortOriginalDict])
    # res=colorAnalyse(img, countFunction=cntf.testFun, reprocessing=[ref.defaultSortOriginalDict])
    # for r in res:
    #     if r[1]>50:
    #         print(r)
    
    res=colorAnalyse(img, countFunction=cntf.testFun, preprocessing=[pref.defaultGaussianBlur], reprocessing=[ref.defaultSortOriginalDict, ref.makeMainColorImg])
    # res=colorAnalyse(img, countFunction=cntf.testFun, reprocessing=[ref.defaultSortOriginalDict, ref.makeMainColorImg])
    cv2.imwrite("result.jpg", res)