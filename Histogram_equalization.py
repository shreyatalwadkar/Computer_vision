import cv2
import matplotlib.pyplot as plt

img = cv2.imread('coins.jpg', cv2.IMREAD_GRAYSCALE)
equalized_img = cv2.equalizeHist(img)

plt.figure(figsize=(10, 5))
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')

plt.tight_layout()
plt.show()
