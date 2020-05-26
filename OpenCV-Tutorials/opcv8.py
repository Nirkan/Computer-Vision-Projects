import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# hsv hue saturation value
	lower_black = np.array([10,10,10])
	upper_black = np.array([100, 100, 100])

	mask = cv2.inRange(hsv, lower_black, upper_black)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	kernel = np.ones((15, 15), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)

	# Removing false positives and negatives
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	
	cv2.imshow('frame', frame)
	cv2.imshow('res', res)
	cv2.imshow('erosion', erosion)
	cv2.dilation('dilation', dilation)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()

