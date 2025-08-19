from kivy.app import App
from kivy.uix.label import Label

class GF07App(App):
    def build(self):
        return Label(text="GF-07 Tracker SMS Forwarder Running...")

if __name__ == "__main__":
    GF07App().run()
