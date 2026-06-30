import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread("shapes.png")
cv2_imshow(img)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([65, 0, 0])
upper_blue = np.array([110, 255, 255])

mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
cv2_imshow(mask)

result = cv2.bitwise_and(img, img, mask=mask)
cv2_imshow(result)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

mask_red = cv2.inRange(hsv_img, lower_red, upper_red)
result_red = cv2.bitwise_and(img, img, mask=mask_red)
cv2_imshow(result_red)
