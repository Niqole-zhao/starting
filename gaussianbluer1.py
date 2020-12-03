#高斯滤波
import cv2
o=cv2.imread("E:\PycharmFiles\huidu\\hudie1.jpg")
r=cv2.GaussianBlur(o,(15,15),0)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()