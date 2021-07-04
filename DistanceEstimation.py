import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(1)
while True:
    ret, frame = cap.read()
    cv.imshow('frame')
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()

