# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:08:36 2017

@author: jxtan
"""

import cv2

img=cv2.imread('baboon.jpg')

cv2.namedWindow('Original image')
cv2.imshow('Original',img)

b,g,r=cv2.split(img)
cv2.imshow("Blue",b)
cv2.imshow("Green", g)
cv2.imshow("Red",r)
cv2.imwrite("Blue.jpg",b)
cv2.imwrite("Green.jpg",g)
cv2.imwrite("Red.jpg",r)
print("RGB value: ",img[20,25])

YCrCb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
y,Cb,Cr=cv2.split(YCrCb)
cv2.imshow("Y",y)
cv2.imshow("Cb", Cb)
cv2.imshow("Cr",Cr)
cv2.imwrite("Y.jpg",y)
cv2.imwrite("Cb.jpg",Cb)
cv2.imwrite("Cr.jpg",Cr)
print("YCrCb value: ",YCrCb[20,25])

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hue,saturation,value=cv2.split(hsv)
cv2.imshow("Hue",hue)
cv2.imshow("Saturation", saturation)
cv2.imshow("Value",value)
cv2.imwrite("Hue.jpg",hue)
cv2.imwrite("Saturation.jpg",saturation)
cv2.imwrite("Value.jpg",value)
print("hsv value: ",hsv[20,25])

cv2.waitKey(0)
