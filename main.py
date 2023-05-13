import os

from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.spinner import MDSpinner

from steamworks import STEAMWORKS as SW

os.environ["KIVY_METRICS_DENSITY"] = "2.5"

STEAMWORKS = SW()
VDF_PATH = f"{os.path.dirname(__file__)}/input.vdf"


class DeckFM(MDBoxLayout):
    orientation = "vertical"
    steam = ObjectProperty(STEAMWORKS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

        # Required to make steam believe it's game by rendering a few frames after start
        load_spinner = MDSpinner()
        self.add_widget(load_spinner)
        Clock.schedule_once(lambda _: self.remove_widget(load_spinner), 1)

    def update(self, dt):
        STEAMWORKS.run_callbacks()
        STEAMWORKS.Input.RunFrame()
        self.canvas.ask_update()


class DeckFMApp(MDApp):
    pass


if __name__ == "__main__":
    STEAMWORKS.initialize()
    STEAMWORKS.Input.Init(True)

    if not STEAMWORKS.Input.SetInputActionManifestFilePath(VDF_PATH):
        raise "cannot load input.vdf"

    app = DeckFMApp()

    app.run()
