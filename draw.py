import cv2
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")
cv2.imshow("Blank_Image",blank)
# image=cv2.imread("cat.jpg")
# cv2.imshow("Cat",image)

blank[200: 300,300: 400]=0,255,0
# cv2.imshow("Green",blank)
cv2.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
# cv2.imshow("Rectangle",blank)
cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=3)
# cv2.imshow("Circle",blank)
cv2.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,0),thickness=3)
cv2.imshow("Line",blank)
cv2.putText(blank,"Hello",(5,255),cv2.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),thickness=4)
cv2.imshow("Text",blank)
cv2.waitKey(0)