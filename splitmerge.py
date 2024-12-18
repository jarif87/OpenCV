import cv2 
import numpy as np

image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)
blank = np.zeros(image.shape[:2], dtype='uint8')
b,g,r = cv2.split(image)

blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

# cv2.imshow('Blue', b)
# cv2.imshow('Green', g)
# cv2.imshow('Red', r)

cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)

print(image.shape)
print(b.shape)
print(g.shape)
print(r.shape)
merged=cv2.merge([b,g,r])
cv2.imshow("Merge",merged)
cv2.waitKey(0)