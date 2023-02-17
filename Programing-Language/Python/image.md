# Intro

+ 模块`cv2`的名字是`opencv-python`

# 图片裁剪
```python
import cv2
imgpath = str()  # 
img = cv2.imread(imgpath)
print(img.shape)
new_img = img[0:img.shape[0] / 2, 0:img.shape[1] / 2]
cv2.imwrite("cropped.jpg", new_img)
```

+ `imread`有两个参数，第二个参数即读取模式（默认1彩色，0灰度模式，-1alpha）
	对应着返回值的`shape`属性即为长宽和模式

# 颜色翻转

## 黑白
```

```

```python
import cv2
# opencv读取图像
img = cv2.imread('E:/liuying/Pictures/lighthouse.png', 1)
print(img.shape)
cv2.imshow('img', img)
img_shape = img.shape  # 图像大小(565, 650, 3)
print(img_shape)
h = img_shape[0]
w = img_shape[1]
# 彩色图像转换为灰度图像（3通道变为1通道）
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
print(gray.shape)
# 最大图像灰度值减去原图像，即可得到反转的图像
dst = 255 - gray
cv2.imshow('dst', dst)
cv2.waitKey(0)


```



## 彩色

```python
import cv2
# opencv读取图像
img = cv2.imread('./Result/1.jpg', 1)
print(img.shape)
cv2.imshow('img', img)
img_shape = img.shape  # 图像大小(565, 650, 3)
print(img_shape)
h = img_shape[0]
w = img_shape[1]
# 最大图像灰度值减去原图像，即可得到反转的图像
dst = 255 - img
cv2.imshow('dst', dst)
cv2.waitKey(0)

```