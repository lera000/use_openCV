import cv2
import matplotlib.pyplot as plt


def viewSimpleImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    print(image.shape)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def viewColorImage(image, name_of_window):
    im_color = image[:, :, [2, 1, 0]]  # convert to rgb-color
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, im_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def viewGrayImage(image, name_of_window):
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    print(image.shape)
    cv2.imshow(name_of_window, im_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


viewSimpleImage(plt.imread("D:/фото/MG_5365.jpg"), "simple photo")
viewColorImage(plt.imread("D:/фото/MG_5365.jpg"), "color photo")
viewGrayImage(plt.imread("D:/фото/MG_5365.jpg"), "gray photo")
