#pip install opencv-contrib-python
import cv2
import numpy as np

#Read Image
plane = r'/Users/farooqueazam/Downloads/Air-New-Zealand-Boeing-747-400.jpg.webp'
img = cv2.imread(plane)
if img is None:
    print('Couldnt', plane)
    exit(0)
print(type(img))
print(img.shape)

#Resize image by width and height
img_200 = cv2.resize(img, (200,150))
#Resize image by scale
img_25 = cv2.resize(img, (0,0), fx=0.25, fy=0.25)


#filters - greyscale, edge detection, bgr to rgb
img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_RGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img_edge = cv2.Canny(img, 100, 200)


#Display image
cv2.imshow('image gray', img_grey)
cv2.imshow('image rgb', img_RGB)
cv2.imshow('image', img)
cv2.imshow('image_edge', img_edge)
cv2.waitKey(0)