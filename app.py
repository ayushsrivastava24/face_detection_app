import streamlit as st
import cv2

st.title("Face Detection using Webcam")

run = st.checkbox("Start Camera")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

frame_window = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()

    if not ret:
        st.write("Camera not working")
        break

  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_window.image(frame)

cap.release()