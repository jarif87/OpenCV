import cv2
import numpy as np

image = cv2.imread("faces.jpeg", 1)
cv2.imshow("Original Image", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("Split Hsv", hsv_split)

ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter", min_sat)

ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter", max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()
