import os
import cv2
import pickle
import mediapipe as mp
import matplotlib.pyplot as plt

DATA_DIR="./Model/data"

data = []
labels = []

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(static_image_mode=True, min_detection_confidence=0.3)

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR,dir_)):
        temp = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        #Facial Landmarks
        results = face_mesh.process(rgbImg)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for i in range(len(face_landmarks.landmark)):
                    x,y  = int(face_landmarks.landmark[i].x * 640), int(face_landmarks.landmark[i].y * 480)
                    temp.append(x)
                    temp.append(y)
                    #cv2.circle(rgbImg, (x,y), 2, (255,0,0), -1)
                    
            data.append(temp)
            labels.append(dir_)

f = open('./Model/data.pickle','wb')
pickle.dump({'data': data, 'labels':labels}, f)
f.close()