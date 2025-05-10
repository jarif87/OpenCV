import numpy as np
import cv2

img = cv2.imread("opencv-logo.png", 1)
print(img)
print(len(img))
print(len(img[0]))
print(len(img[0][0]))
print(img.shape)
print(img.dtype)
print(img[:, :, 1])
print(img.size)
