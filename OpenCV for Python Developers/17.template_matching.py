import numpy as np
import cv2
template = cv2.imread("template.jpg", 0)
player = cv2.imread("players.jpg", 0)
cv2.imshow("Template Original", template)
cv2.imshow("Players", player)

result = cv2.matchTemplate(player, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)
cv2.circle(result, max_loc, 15, 255, 2)

cv2.imshow("Matching", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
