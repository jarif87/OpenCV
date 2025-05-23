import numpy as np
import cv2
image = cv2.imread("detect_blob.png", 1)
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Binary", thresh)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = image.copy()
index = -1
thickness = 4
color = (255, 0, 255)
cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Contours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
