import cv2
import matplotlib.pyplot as plt

# подготовка изображения к изменению, чтобы не было искажений
image = plt.imread("D:/dataset phone/1.jpg")
final_wide = 300
r = float(final_wide) / image.shape[1]
dim = (final_wide, int(image.shape[0] * r))

# уменьшение изображение до подготовленных размеров
resized = cv2.resize(image[:, :, [2, 1, 0]], dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resize image", resized)
cv2.waitKey(0)
