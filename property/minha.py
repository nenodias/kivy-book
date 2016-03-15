# *-* coding: utf-8 *-*
# file: minha.py
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, ObjectProperty, StringProperty

class MinhaSpace(RelativeLayout, EventDispatcher):
    nome = StringProperty('Lol',allownone=True)
    sobrenome = StringProperty('', allownone=True)

    def imprime(self):
        '''
        for item in self.children:
            for campo in item.children:
                print(campo.text)
        '''
        print(self.nome)

    def callback(self, event, propriedade):
        if hasattr(self, propriedade):
            setattr(self, propriedade, event[1])

class MinhaApp(App):
    

    def build(self):
        return MinhaSpace()

if __name__ == '__main__':
    MinhaApp().run()