import cv2
import pickle
import numpy as np
import mediapipe as mp
from flask import Flask, render_template, Response, send_file

model_dict=pickle.load(open('./model.p','rb'))
model=model_dict['model']
labels_dict = {0: 'Hello', 1: 'Goodbye', 2: 'Help'}

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(static_image_mode=False, min_detection_confidence=0.3)

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
        
class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        success, img = self.video.read()
        if success:        
            obj = lipReading()
            obj.start(img)
            ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()

class webServer():
    def __init__(self, *args, **kwargs) -> None:
        self.app = Flask(*args, **kwargs)
        self.register_endpoints()
    
    def gen(self, camera):
        while True:
            frame = camera.get_frame()
            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame
                + b'\r\n\r\n')

    def register_endpoints(self):
        self.app.add_url_rule(rule='/', endpoint='index', view_func=self.index, methods=['GET'])
        self.app.add_url_rule(rule='/manifest.json', endpoint='manifest', view_func=self.serve_manifest, methods=['GET'])
        self.app.add_url_rule(rule='/sw.js', endpoint='sw', view_func=self.serve_sw, methods=['GET'])
        self.app.add_url_rule(rule='/video_feed', endpoint='video_feed', view_func=self.video_feed, methods=['GET'])
        
    def index(self):
        return render_template('index.html')

    def serve_manifest(self):
        return send_file('manifest.json', mimetype='statitc/manifest+json')

    def serve_sw(self):
        return send_file('sw.js', mimetype='application/javascript')

    def video_feed(self):
        return Response(self.gen(VideoCamera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
        
    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)