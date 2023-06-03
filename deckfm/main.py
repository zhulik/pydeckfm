import asyncio
import os
import sys

from input import Input
from logger import Logger

os.environ["KIVY_METRICS_DENSITY"] = "2.5"

LOGGER = Logger()
sys.stdout = LOGGER

from kivy.clock import Clock  # noqa: E402
from kivy.properties import ObjectProperty  # noqa: E402
from kivymd.app import MDApp  # noqa: E402
from kivymd.uix.screen import MDScreen  # noqa: E402
from kivymd.uix.label import MDLabel  # noqa: E402
from kivymd.uix.spinner import MDSpinner  # noqa: E402

from steamworks import STEAMWORKS as SW  # noqa: E402
from steamworks.exceptions import SteamNotRunningException

STEAMWORKS = SW()

try:
    STEAMWORKS.initialize()
except SteamNotRunningException:
    print("STEAM IS NOT RUNNING")


class LogView(MDLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        LOGGER.bind(lines=self._on_logger_lines)

    def _on_logger_lines(self, _, lines):
        self.text = str("\n".join(lines))


class DeckFM(MDScreen):
    orientation = "vertical"
    steam = ObjectProperty(STEAMWORKS)
    input = ObjectProperty(Input(STEAMWORKS.Input))
    logger = ObjectProperty(LOGGER)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

        # Required to make steam believe it's game by rendering a few frames after start
        load_spinner = MDSpinner()
        self.add_widget(load_spinner)
        Clock.schedule_once(lambda _: self.remove_widget(load_spinner), 1)

    def update(self, _dt):
        STEAMWORKS.run_callbacks()
        self.canvas.ask_update()
        self.input.update()


class DeckFMApp(MDApp):
    pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(DeckFMApp().async_run())
    loop.close()
