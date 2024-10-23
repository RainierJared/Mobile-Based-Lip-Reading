import cv2
import pickle
import numpy as np
import mediapipe as mp


model_dict=pickle.load(open('./model.p','rb'))
model=model_dict['model']
labels_dict = {0: 'Hello', 1: 'Goodbye', 2: 'Help'}

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(static_image_mode=True, min_detection_confidence=0.5)

class lipReading():
    global labels_dict, word_read
    data = []
    labels = []
    
    def __init__(self):
        self.temp  = [] 

    def start(self, frame):
        
        #Facial Landmarks
        results = face_mesh.process(frame)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for i in range(len(face_landmarks.landmark)):
                    x,y  = int(face_landmarks.landmark[i].x * 640), int(face_landmarks.landmark[i].y * 480)
                    self.temp.append(x)
                    self.temp.append(y)
                    
                    cv2.circle(frame, (x,y), 2, (255,0,0), 1)
                    
            prediction = model.predict([np.asarray(self.temp)])    
            word_read = labels_dict[int(prediction[0])]
            
            cv2.putText(frame, word_read, (20,40), cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,0),3,cv2.LINE_AA)
        
