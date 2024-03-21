import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

height , width = 720 , 1280
# My WebCam
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

# hand detection
detec1 = HandDetector(maxHands=2,detectionCon=.75)

# communication
sockunity = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverPortAddress = ("127.0.0.1" , 5052 )

while True:
    # Get frame from the webcam
    success, img = cap.read()
    # hands
    hands, img = detec1.findHands(img)

    data = []

    #landmark values (x,y,z)*21  -there are 21 landmarks
    if hands:
        #get the first hand detected
        hand = hands[0]
        #get the landmark list
        lmList = hand['lmList']
        #print(lmList)
        for lm in lmList:
            data.extend([lm[0],height - lm[1],lm[2]])
        #print(data)
        sockunity.sendto(str.encode(str(data)), serverPortAddress)
    img = cv2.resize(img, (0,0),None, 0.5, 0.5)
    cv2.imshow('image',img)
    cv2.waitKey(1)