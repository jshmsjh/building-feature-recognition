# building-feature-recognition

在本项目中，我们使用传统和结合深度学习的方法识别并量化建筑物的特征。包括：楼层数目、最高高度、最宽宽度、 最长长度、窗户数目、窗户面积、整个建筑的体积。

我们的实验报告在`report`文件夹。

## 实验结果

**楼层数目**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 5层    | 6层           | 6层    |
| 实际结果 | 5层    | 6层           | 6层    |

**窗户数目**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 60扇   | 87扇          | 44扇   |
| 实际结果 | 60扇   | 100扇         | 44扇   |

**窗户尺寸**

|          | 商学院        | 学生宿舍5号楼 | 网络楼        |
| -------- | ------------- | ------------- | ------------- |
| 实验结果 | 长6.0m-宽1.9m | 长3.2m-宽1.9m | 长2.6m-宽1.9m |
| 实际结果 | 长4.7m-宽2.1m | 长3.4m-宽1.7m | 长2.6m-宽2.3m |

**窗户面积($m^2$)**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 12     | 6             | 5      |
| 实际结果 | 9.9    | 5.9           | 5.9    |

**最长长度($m$)**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 120    | 35            | 40     |
| 实际结果 | 126    | 36.7          | 45.7   |

最宽宽度($m$)

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 60     | 15            | 18     |
| 实际结果 | 69.7   | 16.3          | 17.9   |

**最高高度($m$)**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 31     | 22            | 19     |
| 实际结果 | 26.2   | 21.1          | 24     |

**建筑物底面积($m^2$)**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 7600   | 1800          | 700    |
| 实际结果 | 7630   | 1599          | 743    |

**整个建筑的体积($m^3$)**

|          | 商学院 | 学生宿舍5号楼 | 网络楼 |
| -------- | ------ | ------------- | ------ |
| 实验结果 | 23.6   | 3.96          | 1.47   |
| 实际结果 | 19.9   | 3.37          | 1.78   |

## 使用代码
#### 边缘检测

##### Sobel算子： 

Sobel算子的优点是方法简单、处理速度快,并且所得的边缘光滑、连续。缺点是边缘较粗，由于处理时需对图像作二值化处理，故得到的边缘与阈值的选取也有很大的关系。 

##### Laplacian算子： 

Laplacian算子的优点是突现出图像中小的细节信息。缺点是对图像中的某些边缘产生双重响应。 

##### Canny算子：  

Canny算子的优点是能够尽可能多地标识出图像中的实际边缘。缺点是图像中的边缘只能标识一次，并且可能错误地将图像噪声标识为边缘。 （在此次实验中由于楼房的棱角和线条过多，导致Canny算子的处理效果并不理想，边缘检测步骤中被首先排除使用）。  

#### 反色：  

反色是与原色叠加可以变为白色的颜色，即用白色(RGB：255，255，255)减去原色的颜色。    

#### 平滑处理：  
当像元放大后,图像的边界就会出现锯齿状，经过增加像元内插处理，加大像元分辨率,使图像细化,即平滑化处理。  

##### 平滑处理效果：  
处理边缘检测后的图片，图片效果中会对边框进行加粗，以此突出每个边框。  

#### 形态学，开运算（先腐蚀后膨胀）去噪：  
对有噪声图象进行开启操作,可选择结构要素矩阵比噪声的尺寸大,因而开启的结果是将背景上的噪声去除。  

#### 轮廓检测函数：  
轮廓检测指在包含目标和背景的数字图像中，忽略背景和目标内部以及噪声干扰的影响，采用一定的技术和方法来实现目标轮廓提取的过程。    

#### 提取图像BGR值：  
在RGB颜色模式中，颜色由红色、绿色、蓝色混合而成。此次实验中特定区域与其余部分存在色差，比如楼顶的颜色浅于地面；窗户的颜色接近黑色，深于楼房墙壁。特定条件下可以选取特定的BGR范围进而选取特定区域。

## 复现

运行代码之前需要确保你的Python已经安装好`cv2`,`numpy`,`matplotlib`包。`demo`文件夹中有需要处理的和处理出的所有图片，`functions`文件夹中包括图像预处理的三个代码。主程序代码在根目录。每个代码都可以独立运行，运行结果会出现在文件夹中。部分注释区包含代码，需要使用者注释已有代码更换注释区代码运行，可以分别查看不同建筑物的实验结果。完整复现过程需要运行预处理代码后运行主程序。  

## 使用自己的图片

替换预处理程序中文件的名称后分别运行预处理程序和主程序。如果默认阈值效果欠佳，可以尝试进行参数的调整。

请注意计算机视觉方法处理时如果要得到确切面积对图片的拍摄角度有一定要求。请尽量保证拍摄的照片是垂直于墙面的。