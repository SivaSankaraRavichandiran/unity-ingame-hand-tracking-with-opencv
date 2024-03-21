import cv2


#cam frame size
height , width = 720 , 1280

# my cam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while True:
    #geting fram from cam
    success , img = cap.read()
    cv2.imshow('img',img)
    cv2.waitKey(1)