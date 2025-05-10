import numpy as np

import cv2

image = cv2.imread("sudoku.png", 0)

cv2.imshow("Original Image", image)

ret, thresh_basic = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("Basic Binary", thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Thresh Adapt", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
