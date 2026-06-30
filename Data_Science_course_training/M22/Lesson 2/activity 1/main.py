import numpy as np
import cv2
import matplotlib.pyplot as plt

emptyImg = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
plt.imshow(emptyImg)
plt.title("Empty Black Canvas")
plt.axis("off")
plt.show()

cv2.line(emptyImg, (0, 0), (511, 511), (255, 0, 0), 3)
cv2.rectangle(emptyImg, (100, 100), (400, 400), (0, 255, 0), 3)
cv2.circle(emptyImg, (256, 256), 80, (0, 0, 255), -1)

plt.imshow(emptyImg)
plt.title("Shapes on Canvas")
plt.axis("off")
plt.show()
