import cv2
import matplotlib.pyplot as plt
import json

# кол-во выводимых изображений
count = 3

cv2.namedWindow("phone in rect", cv2.WINDOW_NORMAL)

for numb in range(1, count):
    json_numb = "D:/dataset phone/{}.json".format(numb)
    with open(json_numb, 'r', encoding='utf-8') as f:
        # достаем данные с json
        text = json.load(f)

    img_numb = plt.imread("D:/dataset phone/{}.jpg".format(numb))
    # рисуем прямоугольник, используя данные с json
    image = cv2.rectangle(img_numb, (text[1][0], text[1][1]), (text[1][2], text[1][3]), (0, 255, 255), 5)
    cv2.imshow("phone in rect", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
