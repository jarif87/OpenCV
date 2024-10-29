import cv2 
import numpy as np

image=cv2.imread("cat.jpg")
cv2.imshow("Cat",image)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)


translated = translate(image, -100, 100)
cv2.imshow('Translated', translated)

def rotate(image,angle,rotpoint=None):
    (height,width)=image.shape[: 2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)

    
    rotmat=cv2.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv2.warpAffine(image,rotmat,dimensions)

rotated = rotate(image, -45)
cv2.imshow('Rotated', rotated)

rotated_rotated = rotate(image, -90)
cv2.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv2.resize(image, (200,200), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Flipping
flip = cv2.flip(image, -1)
cv2.imshow('Flip', flip)

# Cropping
cropped = image[200:400, 300:400]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)