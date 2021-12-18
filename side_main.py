import cv2  #导入opencv模块
import numpy as np
import matplotlib.pyplot as plt

#本程序用于大津算法的实现

#img = cv2.imread("./demo/test3-1.jpg")#(楼层计数)
#img = cv2.imread("./demo/Mask.jpg")#(检测商学院窗户)
img = cv2.imread("./demo/Final.jpg")#(检测网络楼窗户)
#导入图片

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#转换为灰度图

#使用局部阈值的大津算法进行图像二值化
dst = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101, 1)

#全局大津算法，效果较差
#res ,dst = cv2.threshold(gray,0 ,255, cv2.THRESH_OTSU)

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,3))
#形态学去噪（括号内3-5都需要尝试一次，选取效果最好数据）
dst=cv2.morphologyEx(dst,cv2.MORPH_OPEN,element)  
#开运算去噪

contours, hierarchy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
#轮廓检测函数
#method:轮廓近似的方法
#cv2.CHAIN_APPROX_NONE:存储所有的轮廓点
#cv2.CHAIN_APPROX_SIMPLE:压缩水平，垂直和对角线段，只留下端点。 例如矩形轮廓可以用4个点编码。
#cv2.CHAIN_APPROX_TC89_L1,cv2.CHAIN_APPROX_TC89_KCOS:使用Teh-Chini chain近似算法

cv2.drawContours(dst,contours,-1,(20,0,0),2)

count=0 
#方框总数
ares_avrg=0  
#遍历找到的所有方框
for cont in contours:

    ares = cv2.contourArea(cont)
    #计算包围形状的面积

    if ares<750: 
    #(过滤面积小于75的形状)
        continue
    count+=1    
    #总体计数加1
    ares_avrg+=ares

    print("{}-blob:{}".format(count,ares),end="  ") 
    #打印出每个方框的面积

    rect = cv2.boundingRect(cont) 
    #提取矩形坐标

    print("x:{} y:{}".format(rect[0],rect[1])) 
    #打印坐标

    cv2.rectangle(img,rect,(0,0,0xff),2) 
    #绘制矩形

    y=10 if rect[1]<10 else rect[1] 
    #防止编号到图片之外（原y=10）

    cv2.putText(img,str(count),(rect[0],y), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1) 
    #在方框左上角写上编号
    #0.8代表字体大小，1代表字体粗细程度

print("方框平均面积:{}".format(round(ares_avrg/ares,2))) 
#打印出每个方框的面积

cv2.namedWindow("imagshow", 2)   
#创建一个窗口
cv2.imshow('imagshow', img)    
#显示原始图片

cv2.namedWindow("dst", 2)   
#创建一个窗口
cv2.imshow("dst", dst)  
#显示灰度图

#plt.hist(gray.ravel(), 256, [0, 256]) 
#计算灰度直方图
#plt.show()

cv2.waitKey()