import cv2
import numpy as np

image = cv2.imread('car.jfif')
blue, green, red = cv2.split(image)

print("Red starts from here")
print(red)
print("Blue starts from here")
print(blue)
print("Green starts from here")
print(green)

cv2.imshow('Original Image', image)
cv2.imshow('Blue Component', blue)
cv2.imshow('Green Component', green)
cv2.imshow('Red Component', red)

cv2.waitKey(0)
cv2.destroyAllWindows()
