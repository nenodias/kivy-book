# *-* coding: utf-8 *-*
# file: drawining.py
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    pass

class DrawingOrganizedApp(App):
    def build(self):
        return DrawingSpace()

if __name__ == '__main__':
    DrawingOrganizedApp().run()