import os

from kivy.event import EventDispatcher
from kivy.properties import ListProperty

VDF_PATH = f"{os.path.dirname(__file__)}/input.vdf"


class InitError(Exception):
    pass


class Input(EventDispatcher):
    controllers = ListProperty([])

    def __init__(self, steam_input) -> None:
        self.input = steam_input

        steam_input.Init(True)

        if not steam_input.SetInputActionManifestFilePath(VDF_PATH):
            raise InitError("cannot load input.vdf")

    def update(self):
        self.input.RunFrame()
        self.controllers = self.input.GetConnectedControllers()
        self._read_input_data()

    def on_controllers(self, _, controllers):
        handle = self.input.GetActionSetHandle("deckfm")

        for controller in controllers:
            # TODO: if not set yet
            self.input.ActivateActionSet(controller, handle)

    def _read_input_data(self):
        a = self.input.GetDigitalActionHandle("up")
        for controller in self.controllers:
            print(self.input.GetDigitalActionData(controller, a).bState)
