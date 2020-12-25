import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("E:\PycharmFiles\huidu\\mote.jpg",0)
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256)

equ = cv2.equalizeHist(img)
plt.subplot(1, 2, 2)
plt.hist(equ.ravel(), 256)
plt.show()

def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

res = np.hstack((img, equ))
cv_show(res, "res")

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res_clahe = clahe.apply(img)
res = np.hstack((img, equ, res_clahe))
cv_show(res, "res")