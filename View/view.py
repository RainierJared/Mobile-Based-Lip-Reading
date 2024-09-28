import kivy
from kivy.app import App
from kivy import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from ModelView.modelView import mView

class view(App):
    def build(self):
        return BoxLayout()