import cv2 as cv


def nothing(x):
    pass


cv.namedWindow('Binary')
cv.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv.setTrackbarPos('threshold', 'Binary', 167)

img_color = cv.imread('wallpaper-2994965.jpg', cv.IMREAD_COLOR)

cv.imshow('Color', img_color)
cv.waitKey(0)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', img_gray)
cv.waitKey(0)

while True:
    low = cv.getTrackbarPos('threshold', 'Binary')
    ret, img_binary = cv.threshold(img_gray, low, 255, cv.THRESH_BINARY_INV)

    cv.imshow('Binary', img_binary)

    img_result = cv.bitwise_and(img_color, img_color, mask = img_binary)
    cv.imshow('result', img_result)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
