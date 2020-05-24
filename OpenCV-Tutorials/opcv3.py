import numpy as np
import cv2

img = cv2.imread('kingfisher.jpg', cv2.IMREAD_COLOR)

# Draw a line on the image
cv2.line(img, (10,10), (600, 700), (255,255,255), 10)

# Draw a rectangel on the image

cv2.rectangle(img, (10, 15), (250, 300), (155, 100, 10), 5)

# Draw a circle

cv2.circle(img, (225, 335), 100,(0,100, 25) , -1 )

# Draw a polygon

pts = np.array([[10, 10], [25, 30], [50, 65], [70, 80], [80, 10]], np.int32)
cv2.polylines(img, [pts], True, (200,15,100))

# Write a text in the image

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Kingfisher image', (1,100), font, 1, (201, 222, 100), 2, cv2.LINE_AA)

# plotting from cv2

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


