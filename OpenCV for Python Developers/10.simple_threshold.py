import numpy as np
import cv2

image = cv2.imread("detect_blob.png", 0)

cv2.imshow("Original", image)

height, width = image.shape[0: 2]

print(f"Image Shape : {image.shape}")
print("Height :", height)
print("Width :", width)

binary = np.zeros([height, width, 1], "uint8")
thresh = 85

for row in range(0, height):
    for col in range(0, width):
        if image[row][col] > thresh:
            binary[row][col] = 255

cv2.imshow("Slow Binary", binary)


ret, thresh = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow("Cv Threshold", thresh)


cv2.waitKey(0)

cv2.destroyAllWindows()
