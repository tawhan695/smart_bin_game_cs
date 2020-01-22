import numpy as np
import cv2

def Cap():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
    cap.release()
    return img