#!/usr/bin/env python  
  
import numpy as np  
import cv2  

def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade.load('haarcascade_frontalface_default.xml')
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

	#cv2.imshow(gray)

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    result = []
    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result

if __name__ == '__main__':

	result = detectFaces("./temp.jpg")
	if len(result) != 0:
		print('find face')
	else:
		print('no face')	
	#print(result)



