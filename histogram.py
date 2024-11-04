import cv2 
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)
blank = np.zeros(image.shape[:2], dtype='uint8')
mask = cv2.circle(blank, (image.shape[1]//2,image.shape[0]//2), 100, 255, -1)
masked = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('Mask', masked)

# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray)

# gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
# plt.figure(figsize=(8,8))
# plt.title("Grayscale histogram")
# plt.xlabel("bins")
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv2.calcHist([image], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv2.waitKey(0)