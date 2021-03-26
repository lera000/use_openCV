import cv2
import numpy as np

img = cv2.imread('D:/rec.jpg', cv2.IMREAD_UNCHANGED)

# изменение цвета на серый
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = 100
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# создание пустого изображения для контуров
img_contours = np.zeros(img.shape)
# рисовка контуров на пустом изображении
cv2.drawContours(img_contours, contours, 0, (0, 255, 0), 3)
cv2.imwrite('D:/rec1.png', img_contours)
