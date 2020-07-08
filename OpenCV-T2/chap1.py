import cv2

print("Package Imported")


# Image reading and showing

img = cv2.imread('monalisa.png')

cv2.imshow('Output', img)
cv2.waitKey(0)                     # waitKey(0) to keep the output window for infinite time




# Vedio Capture


cap = cv2.VideoCapture('test_video.mp4')

while True:
    success, img  = cap.read()
    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):          # This will close the window on pressing q
        break




# Webcam capture

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break
