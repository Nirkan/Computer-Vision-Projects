# Python version 2.7
# Importing packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading images
img = cv2.imread('kingfisher.jpg', 0)

# Print shape of image
print(img.shape)

# Plotting image using cv2
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plotting in matplotlib
'''
plt.imshow(img, cmap= 'gray', interpolation = 'bicubic')
plt.plot([50, 100], [400, 100], 'c', linewidth = 10)
plt.show()
'''

