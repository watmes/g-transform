#!/usr/local/bin/python
import cv2

image = cv2.imread('raw.jpg')



g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0



# RGB - Green
#cv2.imshow('G-RGB', g)
cv2.imwrite('stripped.jpg', g)

cv2.waitKey(0)
