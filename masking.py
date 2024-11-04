import cv2 
import numpy as np

image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)

blank = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow('Blank Image', blank)

circle = cv2.circle(blank.copy(), (image.shape[1]//2 + 45,image.shape[0]//2), 100, 255, -1)

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv2.bitwise_and(circle,rectangle)
cv2.imshow('Weird Shape', weird_shape)

masked = cv2.bitwise_and(image,image,mask=weird_shape)
cv2.imshow('Weird Shaped Masked Image', masked)
cv2.waitKey(0)