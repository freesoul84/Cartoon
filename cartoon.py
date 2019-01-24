#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:19:01 2019

@author: alkesha
"""
#Importing all files
import cv2

#video capturing
cam=cv2.VideoCapture(0)
while True:
  #frame selection
  c,frame=cam.read()
  frame=cv2.resize(frame,(700,500))
  #conversion of each frame to grey colour
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #blurring of image
  gray = cv2.medianBlur(gray,5,5)
  
  edge= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
  
  bilateral = cv2.bilateralFilter(frame, 5, 300, 300)
  
  cartoon = cv2.bitwise_and(bilateral, bilateral, mask=edge)
  cv2.imshow("Cartoon", cartoon)
  k=cv2.waitKey(1)
  if k==ord("q"):
      break
cam.release()
cv2.destroyAllWindows()

 


 