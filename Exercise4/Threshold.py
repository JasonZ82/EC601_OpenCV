# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:53:16 2017

@author: jxtan
"""

import cv2
import numpy as np

image = cv2.imread("baboon.jpg")
cv2.imshow("Original",image)
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", grayimg)
#binary threshold
ret,thresh=cv2.threshold(grayimg,128,255,2) 
ret,binary_thresh=cv2.threshold(grayimg,128,255,cv2.THRESH_BINARY)
cv2.imshow("binary Image", binary_thresh)
#band threshold
ret,thresh1=cv2.threshold(grayimg,27,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(grayimg,125,255,cv2.THRESH_BINARY_INV)
band_thresh = np.bitwise_and(thresh1,thresh2)
cv2.imshow("band Image", band_thresh)
#semi threshold
ret,thresh3=cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  
semi_thresh = np.bitwise_and(grayimg,thresh3)
cv2.imshow("semi Image", semi_thresh)
#adaptive threshold
adaptive_thresh=cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,101,10)  
cv2.imshow("adaptive Image", adaptive_thresh)

cv2.waitKey(0)