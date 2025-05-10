import cv2
import numpy as np

image = cv2.imread("thresh.jpg")
cv2.imshow("Original", image)

blurr = cv2.GaussianBlur(image, (5, 55), 0)

kernel = np.ones((5, 5), "uint8")
dialate = cv2.dilate(image, kernel, iterations=1)
erode = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Dialate", dialate)
cv2.imshow("Erode", erode)
cv2.imshow("Blurr", blurr)
cv2.waitKey(0)
cv2.destroyAllWindows()
