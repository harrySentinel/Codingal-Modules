import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread("color.jpg")
cv2_imshow(image)
print(image.shape)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_image)
print(gray_image.shape)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2_imshow(hsv_image)
print(hsv_image.shape)

canny_image = cv2.Canny(gray_image, 150, 200)

kernel = np.ones((1, 1), np.uint8)
erode_image = cv2.erode(canny_image, kernel, iterations=1)

kernel1 = np.ones((5, 5), np.uint8)
dilate_image = cv2.dilate(canny_image, kernel1, iterations=1)

hori_display = np.concatenate((canny_image, erode_image, dilate_image), axis=1)
cv2_imshow(hori_display)

image2 = cv2.imread("lion.jpg")
denoise_image = cv2.fastNlMeansDenoisingColored(image2, None, 20, 20, 7, 15)

hori_display2 = np.concatenate((image2, denoise_image), axis=1)
cv2_imshow(hori_display2)
