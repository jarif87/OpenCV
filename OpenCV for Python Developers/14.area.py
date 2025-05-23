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

objects = np.zeros([image.shape[0], image.shape[1], 3], "uint8")
for c in contours:
    cv2.drawContours(objects, [c], -1, color, -1)
    area = cv2.drawContours(objects, [c], -1, color, -1)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    M = cv2.moments(c)
    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])
    cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)
    print(f"Area : {area},Perimeter : {perimeter}")

cv2.imshow("Contours", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
