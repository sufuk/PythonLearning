import cv2
import imutils
import numpy

camera = cv2.VideoCapture(0)
top, right, bottom, left = 10, 350, 225, 590
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
    cv2.imshow('frame', frame)
    roi = frame[top:bottom, right:left]
    gray_image = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('gray_image', thresh1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
