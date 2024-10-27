import cv2 
image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
blur=cv2.GaussianBlur(image,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow("BLUr",blur)
canny=cv2.Canny(image,125,175)
cv2.imshow("Canny",canny)

dialate=cv2.dilate(canny,(3,3),iterations=2)
cv2.imshow("Dialate",dialate)

eroded=cv2.erode(dialate,(3,3),iterations=3)
cv2.imshow("Eroded",eroded)

resize=cv2.resize(image,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow("Resized",resize)

crop=image[50:200,200:400]
cv2.imshow("Croped",crop)
cv2.waitKey(0)
