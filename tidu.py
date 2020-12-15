import cv2

img=cv2.imread("E:\PycharmFiles\huidu\\yuan.jpg",cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
cv_show(sobelx, "sobelx")

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv_show(sobely, "sobely")

sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show(sobelxy, "sobelxy")
