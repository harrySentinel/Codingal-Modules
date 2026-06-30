import cv2
import numpy as np
import matplotlib.pyplot as plt
from vcam import vcam, meshGen

img = cv2.imread("minions.jpg")
H, W = img.shape[:2]

c1 = vcam(H=H, W=W)
plane = meshGen(H, W)

plane.Z += 20 * np.exp(-0.5 * ((plane.X / plane.W) / 0.1) ** 2) / (0.1 * np.sqrt(2 * np.pi))
pts3d = plane.getPlane()
pts3d = c1.project(pts3d)
map_x, map_y = c1.getMaps(pts3d)

output = cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR)

plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Funky Mirror Effect")
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.show()
