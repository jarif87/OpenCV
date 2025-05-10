import numpy as np
import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(0)

color = (0, 255, 0)
line_width = 3
radius = 100
point = (0, 0)


def click(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x, y)
        point = (x, y)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click)

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # If frame is read correctly, resize it
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.circle(frame, point, radius, color, line_width)
        cv2.imshow("Frame", frame)

    # Wait for keypress for 1ms
    ch = cv2.waitKey(1) & 0xFF
    # If 'q' is pressed, break the loop
    if ch == ord("q"):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
