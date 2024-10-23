import os
import cv2
import pickle
import mediapipe as mp
import matplotlib.pyplot as plt

DATA_DIR="./Model/data"

data = []
labels = []

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(static_image_mode=False, min_detection_confidence=0.3)

def data_gather():
        temp = []
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
            
def beginLoop():
    global img
    while True:
        ret,img = cap.read()
        if ret:
            data_gather()
        else:
            break
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break    
            
def start():
    global dir_
    for dir_ in os.listdir(DATA_DIR):
        for path in os.listdir(os.path.join(DATA_DIR,dir_)):
            global cap
            cap = cv2.VideoCapture(os.path.join(DATA_DIR,dir_,path))
            beginLoop()
    
            
if __name__ == "__main__":
    start()
    f = open('./Model/data.pickle','wb')
    pickle.dump({'data': data, 'labels':labels}, f)
    f.close()
    
cap.release()
cv2.destroyAllWindows()