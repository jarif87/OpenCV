import cv2 

# Read and display the image
image = cv2.imread("cat.jpg")
cv2.imshow("Cat", image)

def rescaleFrame(frame, scale=0.40):
    width = int(frame.shape[1] * scale)  # Convert to int
    height = int(frame.shape[0] * scale)  # Convert to int
    dimensions = (width, height)
    
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)



resize_image=rescaleFrame(image)
cv2.imshow("image",resize_image)
# Capture video
capture = cv2.VideoCapture("test.mp4")
while True:
    isTrue, frame = capture.read()
    if not isTrue:  # Check if the frame was read correctly
        break
    
    frame_resize = rescaleFrame(frame)
    cv2.imshow("Video", frame)
    cv2.imshow("Video Resized", frame_resize)
    
    if cv2.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv2.destroyAllWindows()
