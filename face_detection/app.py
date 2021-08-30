#!/usr/bin/env python3

import cv2
import sys
import face_recognition
import os


# Face recognition on original photo 
img = face_recognition.load_image_file('photo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
originalFace = face_recognition.face_locations(img)[0]
encodePhoto = face_recognition.face_encodings(img)[0]
#cv2.rectangle(img,(originalFace[3],originalFace[0]),(originalFace[1],originalFace[2]),(0,255,0),2)

#cv2.imshow('Foto',img)

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(imgS)
    encode = face_recognition.face_encodings(imgS,faces)

    for encodeFace,faceLoc in zip(encode,faces):
        matches = face_recognition.compare_faces([encodePhoto],encodeFace)
        faceDis = face_recognition.face_distance([encodePhoto],encodeFace)
        print(round(faceDis[0],2))

        if round(faceDis[0],2) < 0.60:
            name = "Diogo Marta"
            y1,x2,y2,x1 = faceLoc
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(frame,name,(x1-6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv2.imshow('Input', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
img.release()
cv2.destroyAllWindows()