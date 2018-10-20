import cv2
import numpy as np
import matplotlib.pyplot as plt

def findholes_f():
    image = cv2.imread('stripped.jpg')
    bad_pixels = []
    bad_pixel_num = 0
    
    r = 0
    c = 0
    while r<400:
        while c<700:
            pixel = image[r,c,1]
        #   g = pixel[1]
            if (pixel < 30):
                bad_pixels.append(r)
                bad_pixels.append(c)
                bad_pixel_num = bad_pixel_num + 1
            c = c + 1
        r = r+1
        c = 0
    print ("found ", bad_pixel_num , " bad pixels")
    return bad_pixels
