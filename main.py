import os

os.environ["KIVY_METRICS_DENSITY"] = "2.5"

from kivy.clock import Clock  # noqa: E402
from kivy.properties import ListProperty, ObjectProperty  # noqa: E402
from kivymd.app import MDApp  # noqa: E402
from kivymd.uix.boxlayout import MDBoxLayout  # noqa: E402
from kivymd.uix.spinner import MDSpinner  # noqa: E402

from steamworks import STEAMWORKS as SW  # noqa: E402

STEAMWORKS = SW()
VDF_PATH = f"{os.path.dirname(__file__)}/input.vdf"


class DeckFM(MDBoxLayout):
    orientation = "vertical"
    steam = ObjectProperty(STEAMWORKS)
    controllers = ListProperty([])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

        # Required to make steam believe it's game by rendering a few frames after start
        load_spinner = MDSpinner()
        self.add_widget(load_spinner)
        Clock.schedule_once(lambda _: self.remove_widget(load_spinner), 1)

    def on_controllers(self, _, controllers):
        handle = STEAMWORKS.Input.GetActionSetHandle("deckfm")

        for controller in controllers:
            # TODO: if not set yet
            STEAMWORKS.Input.ActivateActionSet(controller, handle)

    def update(self, dt):
        STEAMWORKS.run_callbacks()
        STEAMWORKS.Input.RunFrame()
        self.controllers = STEAMWORKS.Input.GetConnectedControllers()
        self.canvas.ask_update()

        a = STEAMWORKS.Input.GetDigitalActionHandle("up")
        for controller in self.controllers:
            print(STEAMWORKS.Input.GetDigitalActionData(controller, a).bState)


class DeckFMApp(MDApp):
    pass


if __name__ == "__main__":
    STEAMWORKS.initialize()
    STEAMWORKS.Input.Init(True)

    if not STEAMWORKS.Input.SetInputActionManifestFilePath(VDF_PATH):
        raise "cannot load input.vdf"

    app = DeckFMApp()

    app.run()
