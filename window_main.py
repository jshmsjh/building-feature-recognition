import cv2
import numpy

image = cv2.imread("./demo/test.jpg")
#image = cv2.imread("DJI_0966.JPG")
print(image[0][0])
BGR = numpy.array([74,73,68])
#需要提取的部分对应的图像BGR值

upper = BGR + 70
#上限200-250，主要是让白色部分多
lower = BGR - 70
#下线可以尝试更高0-10，目的是框出整体
mask = cv2.inRange(image,lower,upper)

cv2.imshow("Mask",mask)
cv2.imwrite("Mask.jpg",mask)
cv2.waitKey(0)

#(_,contours,hierarchy) = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours , hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("number of contours: %d" % (len(contours)))

allBuildingsImage = image.copy()
cv2.drawContours(allBuildingsImage,contours,-1,(0,0,255),2)
cv2.imshow("Image of the building",allBuildingsImage)
cv2.waitKey(0)

theonlybuilding = image.copy()
contours = list(contours)
# print(type(contours))
contours.sort(key=len,reverse=True)
cv2.drawContours(theonlybuilding,[contours[0]],-1,(0,0,255),2)

cv2.imshow("the building",theonlybuilding)
cv2.imwrite("the building.jpg",theonlybuilding)
cv2.waitKey(0)

#获取最终方框框取的面积
#ares = cv2.contourArea(theonlybuilding)
#print("{}-blob:{}".format(theonlybuilding,ares),end="  ")