import cv2 
image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

threshold,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("simple threshold",thresh)


threshold,thresh_inv=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshold_INV",thresh_inv)

adaptive_thres=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow("Adaptive_threshold",adaptive_thres)
cv2.waitKey(0)