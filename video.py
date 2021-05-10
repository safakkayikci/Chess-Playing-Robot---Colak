import time

import os
import cv2

# cap = cv2.VideoCapture("http://192.168.1.1:8080/video")
cap = cv2.VideoCapture(2)
timer_a = time.time()

while True:
    ret, frame = cap.read()

    img = cv2.resize(frame, (800, 600))
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# a =  os.system("python3 /root/Desktop/untitled/face_classification/src/video_emotion_color_demo.py")

cv2.destroyAllWindows()
