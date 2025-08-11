import cv2
import numpy as np

image = cv2.imread('coins.jpg')
negative_image = cv2.bitwise_not(image)

cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
