from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Acrescentar(BoxLayout):
    pass

class Contador(App):
    def build(self):
        return Acrescentar()

Contador().run()
