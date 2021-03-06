import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("E:\PycharmFiles\huidu\\shiyishi-1.jpg")
hist = cv2.calcHist([img], [0], None, [256], [0,256])
print(hist.shape)
print(img.shape)
plt.hist(img.ravel(), 256)
#plt.show()

color = ("b", "g", "r")
for i,col in enumerate(color):
    histr = cv2.calcHist([img], [i],None, [256], [0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])

def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
# cv_show(mask, "mask")
img = cv2.imread("E:\PycharmFiles\huidu\\shiyishi-1.jpg",0)
# cv_show(img, "img")
masked_img = cv2.bitwise_and(img, img, mask=mask)    #
# cv_show(masked_img, "masked_img")
hist_full = cv2.calcHist([img], [0], None, [256], [0,256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0,256])
plt.subplot(221), plt.imshow(img, "gray")
plt.subplot(222), plt.imshow(mask, "gray")
plt.subplot(223), plt.imshow(masked_img, "gray")
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0, 256])
plt.show()