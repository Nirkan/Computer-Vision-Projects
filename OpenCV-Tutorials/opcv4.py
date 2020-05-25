import numpy as np
import cv2

img = cv2.imread('kingfisher.jpg', cv2.IMREAD_COLOR)

px = img[125, 125]

img[125, 125] = [0, 0, 0]

px = img[125, 125]

print(px)

# Region of an image ROI

roi = img[100:300, 100:200]

img[100:300, 100:300] = [0,100,0]

# Copying a region from image and paste it.

kingfisher = img[320:400, 320:400]
img[0:80, 0:80] = kingfisher

# plot the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

