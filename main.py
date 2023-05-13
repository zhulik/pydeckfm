import os

from steamworks import STEAMWORKS

steamworks = STEAMWORKS()
steamworks.initialize()

steamworks.Input.Init(True)

os.environ['KIVY_METRICS_DENSITY'] = '2.5'

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class DeckFM(MDBoxLayout):
    orientation = "vertical"

    steam = ObjectProperty(steamworks)


class DemoApp(MDApp):
    def update(self, dt):
        steamworks.Input.RunFrame()


if __name__ == '__main__':
    app = DemoApp()
    Clock.schedule_interval(app.update, 0.1)
    app.run()
