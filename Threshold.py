import cv2
import numpy as np

img = cv2.imread('coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
