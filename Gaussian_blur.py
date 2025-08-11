import cv2
import numpy as np

def estimate_background_gaussian_blur(image, kernel_size=(21, 21),
sigmaX=0):
    blurred_image = cv2.GaussianBlur(image, kernel_size, sigmaX)
    return blurred_image
                                        
image = cv2.imread('coins.jpg')
background = estimate_background_gaussian_blur(image)

cv2.imshow('Original Image', image)
cv2.imshow('Estimated Background', background)
cv2.waitKey(0)
cv2.destroyAllWindows()
