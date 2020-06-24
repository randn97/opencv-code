Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cv2
img = cv2.imread('C:/Users/Stars/Pictures/taifuni.jpg',10)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('C:/Users/Stars/Pictures/taifuni.png',img)
cv2.destroyAllWindows()
