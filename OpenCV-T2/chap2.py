import cv2
import numpy as np

img = cv2.imread('monalisa.png')

kernel = np.ones((5,5), np.uint8)

# Grayscale Image

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurring the Image

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

# Canny Edge Detection

imgCanny = cv2.Canny(img, 150, 200)

# Dilate the image

imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)

# Erode the Dilated Image

imgEroded = cv2.erode(imgDilation, kernel, iterations  = 1)


# Image Visualization

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Erosion Image", imgEroded)

# Infinite(0) waitkey for image window. Press q to exit.

cv2.waitKey(0) 
