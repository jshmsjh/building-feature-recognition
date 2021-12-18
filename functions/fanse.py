import cv2
#调用opencv包

src=cv2.imread("./demo/test4-1.jpg",1)
print(src.shape)
#输出图像数据
Img=255-src
#反色

print(Img.shape)
cv2.imshow("Img",Img)
#输出反色图像

cv2.imshow("src",src)
#输出原图像

cv2.imwrite('final.jpg',Img)
cv2.waitKey(0)