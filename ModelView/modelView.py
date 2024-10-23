import cv2
import numpy as np

class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        success, img = self.video.read()
        success, jpeg = cv2.imencode('.jpg', img)
        
        return jpeg.tobytes()