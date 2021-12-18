import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./demo/laplacian1.jpg')
kernel = np.ones((20,20),np.float32)/50
#平滑处理中(20,20)经测试效果最好
dst = cv.filter2D(img,-1,kernel)

#plt.subplot(121)
#plt.imshow(img)
#plt.title('Original')
#plt.xticks([])
#plt.yticks([])
#plt.subplot(122)

plt.imshow(dst)
plt.title('Averaging')
plt.show()
