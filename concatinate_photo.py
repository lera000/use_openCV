import numpy as np
import matplotlib.pyplot as plt
import cv2

# горизонтальное объединение изображений
img1 = plt.imread("D:/dataset phone/1.jpg")
img2 = plt.imread("D:/dataset phone/2.jpg")
vis = np.concatenate((img1[:, :, [2, 1, 0]], img2[:, :, [2, 1, 0]]), axis=1)
cv2.imwrite('D:/out.png', vis)
