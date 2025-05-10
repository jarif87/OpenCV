import numpy as np
import cv2

image = cv2.imread("players.jpg")

cv2.imshow("Original", image)
# scale
image_half = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
image_stretch = cv2.resize(image, (600, 600))
image_stretch_near = cv2.resize(
    image, (600, 600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", image_half)
cv2.imshow("Image Stretch", image_stretch)
cv2.imshow("Image Stretch Near", image_stretch_near)
# rotation

M = cv2.getRotationMatrix2D((0, 0), -30, 1)
rotate = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Rotate", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
