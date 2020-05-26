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

	## Average the frame
	kernel = np.ones((10, 10), np.float32)/100
	smoothed = cv2.filter2D(res, -1, kernel)

	## Gaussian blur
	blur = cv2.GaussianBlur(res,(15,15),0)
	median = cv2.medianBlur(res, 10)
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)

	cv2.imshow('frame', frame)
	#cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	#cv2.imshow('smoothed', smoothed)
	cv2.imshow('blur', blur)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()

