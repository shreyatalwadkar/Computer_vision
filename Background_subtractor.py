import cv2

image = cv2.imread('coins.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bg_subtractor = cv2.createBackgroundSubtractorMOG2()
fg_mask = bg_subtractor.apply(gray)
foreground = cv2.bitwise_and(image, image, mask=fg_mask)

cv2.imshow('Original Image', image)
cv2.imshow('Foreground', foreground)

cv2.waitKey(0)
cv2.destroyAllWindows()
