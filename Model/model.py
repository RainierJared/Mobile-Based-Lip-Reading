import cv2
import numpy as np
from cv2 import face
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpFace = mp.solutions.face_mesh
faceMarks = mpFace.FaceMesh()
    
cap = cv2.VideoCapture(0)    
class lipReadModel():
    def __init__(self):
        self.lipread=self
        
    def faceDetect(camera):
        cap = cv2.VideoCapture(camera)    
        while True:
            success, img = cap.read()
            if not success:
                break
            #print('Face detected: '+ str(success))
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            landmarks = faceMarks.process(imgRGB)
            #print(landmarks.multi_face_landmarks)
            
            if landmarks.multi_face_landmarks:
                for kpts in landmarks.multi_face_landmarks:
                    mpDraw.draw_landmarks(img, kpts, mpFace.FACEMESH_CONTOURS)