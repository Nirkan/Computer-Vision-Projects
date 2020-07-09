import cv2
import numpy as np

img = cv2.imread('monalisa.png')
print(img.shape)

# Resizing the image

imgResize = cv2.resize(img, (150, 150))
print(imgResize.shape)


 # Here we have height first and then the width
 # In openCV width comes first and then the height

imgCropped  = img[0:200, 100:250 ]  


# Displaying the images

cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)

