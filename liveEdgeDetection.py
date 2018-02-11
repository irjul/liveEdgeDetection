#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:44:25 2018

@author: PraveenKumar
"""

import cv2
def sketch(gray,frame):
    
    img_gray_blur = cv2.GaussianBlur(gray, (5,5),0)
    canny_edges = cv2.Canny(img_gray_blur,10,70)
    ret, mask = cv2.threshold(canny_edges, 70,255,cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = sketch(gray,frame)
    cv2.imshow("Live Sketch", canvas)
    if cv2.waitKey(1) == 13:
        break
    
cap.release()
cv2.destroyAllWindows()