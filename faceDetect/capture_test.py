import cv2
import numpy as np
import time
import signal
import sys
'''
cap = cv2.VideoCapture(0)
print cap.isOpened()
ret, frame = cap.read()
print ret
cv2.imwrite('temp.jpg',frame)
cap.release()
'''
def handler(signal_num, frame):
    print 'you pressed ctrl + c!'
    cap.release()
    sys.exit(signal_num)

signal.signal(signal.SIGINT,handler)

cap = cv2.VideoCapture(0)

def capture():
    ret, frame = cap.read()
    cv2.imwrite('temp.jpg',frame)
    print ret
    print cap.isOpened()
    return ret and cap.isOpened()


while True:
    ret1 = capture()
    print ret1
    time.sleep(1)
