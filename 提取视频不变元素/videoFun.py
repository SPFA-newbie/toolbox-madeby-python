import cv2 as cv
import imgFun as tool

# capture       cv.VideoCapture(目标视频)
# interval      每多少帧采样一次
# replace       使用什么像素替换不同的部分
# maxD          像素的最大容差
# blur          帧的处理方法（默认高斯卷积）
def findStaticPixelInVideo(capture, interval=1, replace=(0, 255, 0), maxD=(32, 32, 32), blur=tool.defaultGaussianBlur):
    hasFrame, result=capture.read()
    if blur!=None:
        result=blur(result)
    i=0
    while hasFrame:
        i=i+1
        hasFrame, frame=capture.read()
        if i%interval==0 and hasFrame:
            if blur!=None:
                frame=blur(frame)
            result=tool.findSamePixel(result, frame, replace, maxD, None)
            print("完成第", i, "帧比对工作")
    return result

if __name__=="__main__":
    result=findStaticPixelInVideo(cv.VideoCapture("test.mp4"), 12)
    cv.imwrite("video_result.jpg", result)