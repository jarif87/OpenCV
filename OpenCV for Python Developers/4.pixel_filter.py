import cv2
img = cv2.imread("butterfly.jpg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray_image.jpg", gray)
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
rgba = cv2.merge((b, g, r, g))
cv2.imwrite("rgba.png", rgba)
cv2.imshow("RGBA Image", rgba)
cv2.imshow("Gray Image", gray)

cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
