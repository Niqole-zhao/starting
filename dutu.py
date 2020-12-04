import cv2  #格式为BGR
import matplotlib.pyplot as plt
import numpy as np

#读取灰度图，即先将彩色图变为灰度图
# img=cv2.imread("E:\PycharmFiles\huidu\\chuanghu1.jpg",cv2.IMREAD_GRAYSCALE)
#读取彩色图
# img=cv2.imread("E:\PycharmFiles\huidu\\shiyishi-1.jpg")

# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# def cv_show(name,img):     #定义一个关于上面展示的函数，即创建一个窗口展示结果
#     cv2.imshow(name,img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# img.shape   #shape属性展示(h,w,c)即宽度，高和颜色通道

#截取某一部分图像
# chuang=img[0:200,0:200]
# cv2.imshow("c",chuang)

#颜色通道提取
# b,g,r = cv2.split(img)
#只保留某一颜色通道
# cur_img = img.copy()
# cur_img[:, :, 0] = 0
# cur_img[:, :, 2] = 0   #修改2来改变颜色通道，R1，G0,B2
# cv2.imshow("b",  cur_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#数值计算
img_c1=cv2.imread("E:\PycharmFiles\huidu\\hudie1.jpg")
img_c2 = img_c1 + 10
print(img_c1[:5, :, 1])