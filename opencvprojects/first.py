import cv2
import os
import numpy as np

image = cv2.imread('image.png', 0)
window_name = 'image'
h, w = image.shape[:2]
#(B, G, R) = image[100, 100]
#B = image[100, 100, 0]

print("Height = {}, Width = {}".format(h, w))
#print("R = {}, G = {}, B = {}".format(R, G, B))

roi = image[0 : 478, 0 : 383]
resize = cv2.resize(image, (470, 380))
filename = 'savedImage.png'
cv2.imwrite(filename, resize)

output = image.copy()
# Using the rectangle() function to create a rectangle.
start_point = (5, 5)
end_point = (300, 100)
color = (255, 0, 0)
thickness = 2
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow(window_name, image)


#cv2.imshow(window_name, roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
