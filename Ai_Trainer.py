import cv2 
import numpy as np  
import time  
import PoseModule as pm

cap = cv2.VideoCapture("ai-trainer/1_1.mp4") 
detector = pm.poseDetector()
while True:
    success, img = cap.read() 
    img = cv2.resize(img, (1280,720))  
    # img = cv2.imread("ai-trainer/test.png")

    img = detector.findPose(img,False) 
    lmlist = detector.findPosition(img,False)
    

    if len(lmlist) != 0:
        # right arm
        detector.findAngle(img,12,14,16)

        # lef arm
        detector.findAngle(img,11,13,15)


    cv2.imshow("Image", img) 
    cv2.waitKey(1)

# 27