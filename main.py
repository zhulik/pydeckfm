import os
os.environ['KIVY_METRICS_DENSITY'] = '2.5'

from steamworks import STEAMWORKS as SW

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


STEAMWORKS = SW()
VDF_PATH = vdf_path = f"{os.path.dirname(__file__)}/input.vdf"


class DeckFM(MDBoxLayout):
    orientation = "vertical"

    steam = ObjectProperty(STEAMWORKS)


class DemoApp(MDApp):
    def update(self, dt):
        STEAMWORKS.run_callbacks()
        STEAMWORKS.Input.RunFrame()


if __name__ == '__main__':
    STEAMWORKS.initialize()
    STEAMWORKS.Input.Init(True)

    if not STEAMWORKS.Input.SetInputActionManifestFilePath(VDF_PATH):
        raise "cannot load input.vdf"

    app = DemoApp()
    Clock.schedule_interval(app.update, 1.0 / 60.0)
    app.run()
