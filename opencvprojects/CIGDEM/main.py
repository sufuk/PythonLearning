import cv2
import imutils
import numpy

camera = cv2.VideoCapture(0)
while(True):
    ret, frame = camera.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
