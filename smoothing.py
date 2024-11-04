import cv2 
import numpy as np

image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)

average=cv2.blur(image,ksize=(7,7))
cv2.imshow("Image_Average",average)


gauss=cv2.GaussianBlur(image,(7,7), 0)
cv2.imshow("Gauss",gauss)

median=cv2.medianBlur(image,3)
cv2.imshow("Median",median)

bilateral=cv2.bilateralFilter(image,10,15,15)
cv2.imshow("Bilateral",bilateral)

cv2.waitKey(0)