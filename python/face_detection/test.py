#!/usr/bin/env python3

import cv2
import sys
import face_recognition


cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# Face recognition on original photo 
img = face_recognition.load_image_file('photo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faceloc = face_recognition.face_locations(img)[0]
encodefoto = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(0,255,0),2)

cv2.imshow('Foto',img)

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
img.release()
cv2.destroyAllWindows()