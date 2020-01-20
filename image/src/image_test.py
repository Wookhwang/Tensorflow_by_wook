import cv2

img_color = cv2.imread('wallpaper-2996530.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Show image')
cv2.imshow('Show image', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow("show GrayScale Image", img_gray)
cv2.waitKey(0)

cv2.imwrite('wallpaper-2996530.jpg', img_gray)

cv2.destroyAllWindows()