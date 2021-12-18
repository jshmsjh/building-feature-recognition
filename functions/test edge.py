#本程序用于边缘检测
import cv2  
#导入opencv模块
import numpy as np

img = cv2.imread("./demo/test4.jpg")
#导入图片，图片放在程序所在目录

#高斯模糊
blurred = cv2.GaussianBlur(img, (3, 3), 0)
#转换为灰度图
out_img_GRAY=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
#将图片转换为灰度图
cv2.namedWindow("img_GRAY", 2)   
#创建一个窗口
cv2.imshow('img_GRAY',out_img_GRAY)
#显示原始图片

#使用sobelx算子进行边缘检测
sobelx = cv2.Sobel(out_img_GRAY,-1,1,0,ksize=3)
cv2.namedWindow("sobelx", 2)   
#创建一个窗口
cv2.imshow('sobelx', sobelx)    
#显示原始图片
cv2.imwrite('sobelx.jpg', sobelx) 
#效果比较理想，保存

"""
# 利用Sobel方法可以进行sobel边缘检测
# img表示源图像，即进行边缘检测的图像
# cv2.CV_64F表示64位浮点数即64float。
# 这里不使用numpy.float64，因为可能会发生溢出现象。用cv的数据则会自动
# 第三和第四个参数分别是对X和Y方向的导数（即dx,dy），对于图像来说就是差分，这里1表示对X求偏导（差分），0表示不对Y求导（差分）。其中，X还可以求2次导。
# 注意：对X求导就是检测X方向上是否有边缘。
# 第五个参数ksize是指核的大小。
"""


#使用laplacian算子进行边缘检测
laplacian = cv2.Laplacian(out_img_GRAY,-5)
cv2.namedWindow("laplacian", 2)   
#创建一个窗口
cv2.imshow('laplacian', laplacian)    
#显示原始图片
cv2.imwrite('laplacian.jpg', laplacian) 
#效果比较理想，保存

"""
#使用laplacian算子进行边缘检测
laplacian = cv2.Log(out_img_GRAY,-1)
cv2.namedWindow("laplacian", 2)   #创建一个窗口
cv2.imshow('laplacian', laplacian)    #显示原始图片
"""
cv2.waitKey()

