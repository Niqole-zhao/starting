import cv2

img = cv2.imread("E:\PycharmFiles\huidu\\b1.jpg")   #输入图片为灰度图
cv2.imshow("hui", img)

blur = cv2.blur(img, (3, 3))
cv2.imshow("jun", blur)

aussian = cv2.GaussianBlur(img, (5, 5), 1)
cv2.imshow("gao", blur)

median = cv2.medianBlur(img, 5)
cv2.imshow("zhon", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()