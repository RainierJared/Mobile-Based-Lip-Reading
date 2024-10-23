from flask import Flask, render_template, Response, send_file
from ModelView.modelView import VideoCamera

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