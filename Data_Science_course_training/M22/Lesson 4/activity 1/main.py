import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img = cv2.imread("shapes.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    n = len(approx)
    if n == 6:
        print("Hexagon detected")
        cv2.drawContours(img, [cnt], 0, (255, 0, 0), 10)
    elif n == 3:
        print("Triangle detected")
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
    elif n > 9:
        print("Circle detected")
        cv2.drawContours(img, [cnt], 0, (0, 255, 255), 3)
    elif n == 4:
        print("Square/Rectangle detected")
        cv2.drawContours(img, [cnt], 0, (255, 255, 0), 3)

cv2_imshow(img)
