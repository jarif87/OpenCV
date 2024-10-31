import cv2 
# import matplotlib.pyplot as plt

image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV_FULL)
cv2.imshow("HSV",hsv)

lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",lab)

rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",rgb)

hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("HSV2BGR",hsv_bgr)
cv2.waitKey(0)