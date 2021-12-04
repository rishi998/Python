from kivy.app import App
from kivy.uix.widget import Widget

class ponggame(Widget):
    pass

class pongapp(App):
    def build(self):
        return ponggame()

pongapp().run()