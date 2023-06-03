import os

import vdf
from kivy.event import EventDispatcher
from kivy.properties import DictProperty, ListProperty

VDF_PATH = f"{os.path.dirname(__file__)}/input.vdf"

class Input(EventDispatcher):
    controllers = ListProperty()
    digital_actions = DictProperty()
    ready = False

    def __init__(self, steam_input) -> None:
        EventDispatcher.__init__(self)
        self.input = steam_input

        self.ready = steam_input.Init(True)

        self.ready = steam_input.SetInputActionManifestFilePath(VDF_PATH)

        with open(VDF_PATH, encoding="utf-8") as file:
            self.manifest = vdf.parse(file)["Action Manifest"]

        actions = self.manifest["actions"]["deckfm"]
        layers = self.manifest["action_layers"]

        buttons = list(actions["Button"].keys()) + [list(l['Button'].keys())[0] for l in layers.values()]
        self.digital_action_handles = {k: self.input.GetDigitalActionHandle(k) for k in buttons}

        print(buttons)

    def on_digital_actions(self, _, actions):
        print(actions)

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
        res = {}
        for controller in self.controllers:
            for name, handle in self.digital_action_handles.items():
                res[name] = self.input.GetDigitalActionData(controller, handle).bState

        self.digital_actions = res
