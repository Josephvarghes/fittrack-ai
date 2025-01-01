import cv2 
import numpy as np  
import time  
import PoseModule as pm

# cap = cv2.VideoCapture("ai-trainer/1_1.mp4") 
detector = pm.poseDetector()
while True:
    # success, img = cap.read() 
    # img = cv2.resize(img, (1280,720))  
    img = cv2.imread("ai-trainer/test.png")

    img = detector.findPose(img) 
    lmlist = detector.findPosition(img,False)
    # print(lmlist) 

    if len(lmlist) != 0:
        pass 
    


    cv2.imshow("Image", img) 
    cv2.waitKey(1)