import numpy as np
import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(0)

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
        cv2.imshow("Frame", frame)

    # Wait for keypress for 1ms
    ch = cv2.waitKey(1) & 0xFF
    # If 'q' is pressed, break the loop
    if ch == ord("q"):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
