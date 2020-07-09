import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# coloring the parts of image

img[:] = 255, 0, 0
img[100:200, 150:250] = 100,20,0


# Drawing a line
# In openCV height and width have different positons 

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,200,0), 5)


# Drawing rectangle

cv2.rectangle(img, (75,85), (150, 150), (210,155,0), 4)



# Drawing Circle

cv2.circle(img, (200,200), 30, (255, 255, 0), 3)



# Adding Text

cv2.putText(img, " OpenCV ", (280, 280), cv2.FONT_HERSHEY_COMPLEX, 0.7, (100, 200, 211), 4)

cv2.imshow("Image", img)

cv2.waitKey(0)