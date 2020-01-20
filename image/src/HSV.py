import cv2 as cv
import numpy as np
'''

color = [255, 0, 0]
pixel = np.uint8([[color]])

hsv = cv.cvtColor(pixel, cv.COLOR_BGR2HSV)
hsv = hsv[0][0]


print("bgr : ", color)
print("hsv : ", hsv)
'''

img_color = cv.imread('wallpaper-2994965.jpg')
height, width = img_color.shape[:2]

img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

lower_blue = (120-50, 30, 30)
upper_blue = (120+50, 255, 255)
img_mask = cv.inRange(img_hsv, lower_blue, upper_blue)

img_result = cv.bitwise_and(img_color, img_color, mask = img_mask)

cv.imshow('img_color', img_color)
cv.imshow('img_mask', img_mask)
cv.imshow('img_result', img_result)

cv.waitKey(0)
cv.destroyAllWindows()

