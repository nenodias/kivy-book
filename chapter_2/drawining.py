# *-* coding: utf-8 *-*
# file: drawining.py
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawiningSpace(RelativeLayout):
    pass

class DrawiningApp(App):
    def build(self):
        return DrawiningSpace()

if __name__ == '__main__':
    DrawiningApp().run()