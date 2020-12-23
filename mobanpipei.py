import cv2
import matplotlib.pyplot as plt
import numpy as np

# img = cv2.imread("E:\PycharmFiles\huidu\\mote.jpg", 0)
# tem = cv2.imread("E:\PycharmFiles\huidu\\lian.jpg", 0)
# h, w = tem.shape[:2]
# print(img.shape)
# print(tem.shape)
#
# methods = ["cv2.TM_CCOEFF", "cv2.TM_SQDIFF","cv2.TM_CCOEFF_NORMED"]
# res = cv2.matchTemplate(img, tem, cv2.TM_SQDIFF)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# print(res.shape)
# print(min_val, min_loc, max_val, max_loc)
#
# for meth in methods:
#     img2= img.copy()
#     #匹配方法的真值
#     method = eval(meth)
#     print(method)
#
#     res = cv2.matchTemplate(img, tem, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     #平方差匹配时取最小值
#     if method in[cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = max_loc
#     else:
#         top_left = max_loc
#     bottcm_right = (top_left[0]+w, top_left[1]+h)
#     #画矩形
#     cv2.rectangle(img2, top_left, bottcm_right, 255, 2)   #创建随机颜色边界框
#     plt.subplot(121), plt.imshow(res  )
#     plt.subplot(122), plt.imshow(img2  )
#     plt.suptitle(meth)
#     plt.show()


#匹配多个对象
img_rgb = cv2.imread("E:\PycharmFiles\huidu\\df.jpg", 0)
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BAYER_BG2GRAY)
tem = cv2.imread("E:\PycharmFiles\huidu\\137.jpg", 0)
h, w = tem.shape[:2]
res = cv2.matchTemplate(img_gray, tem, cv2.TM_SQDIFF_NORMED)
threshold = 0.1
max_val = 1
while max_val > threshold:
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val > threshold:
        res[max_loc[1] - h // 2:max_loc[1] + h // 2 + 1, max_loc[0] - w // 2:max_loc[0] + w // 2 + 1] = 0
        img_rgb = cv2.rectangle(img_rgb, (max_loc[0], max_loc[1]), (max_loc[0] + w + 1, max_loc[1] + h + 1), (0, 255, 0))
    cv2.imwrite('output.png', img_rgb)

loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    bottom_right = (pt[0] + w.pt[1]+h)
    cv2.rectangle(img_rgb, pt.bottom_right, (0,0,255), 2)
cv2.imshow("img_rgb", img_rgb)
cv2.waitKey(0)