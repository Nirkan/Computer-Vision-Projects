## Change the perpective of your image. Getting the birds eye view.


import cv2
import numpy as np

# Reading Image

img = cv2.imread('cards.jpg')


# Width and Height of Output image

width, height = 200,300


# Points and Region of Interest

pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])

# Frame for Output image

pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])

# Perspective Transform

matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Warp Perspective for Output image

imgOutput  = cv2.warpPerspective(img, matrix, (width, height))


# Displying the Image

cv2.imshow("Image", img)

cv2.imshow("Output", imgOutput)

cv2.waitKey(0)