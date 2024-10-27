import cv2 
# image=cv2.imread("cat.jpg")
# cv2.imshow("Cat",image)
# cv2.waitKey(0)

capture=cv2.VideoCapture("test.mp4")
while True:
    isTrue,frame=capture.read()
    cv2.imshow("Video",frame)
    if cv2.waitKey(20) & 0xFF==ord("d"):
        break
capture.release()
cv2.destroyAllWindows()