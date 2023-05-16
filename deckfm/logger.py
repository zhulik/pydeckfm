import sys

from kivy.event import EventDispatcher
from kivy.properties import ListProperty


class Logger(EventDispatcher):
    lines = ListProperty()

    def __init__(self):
        EventDispatcher.__init__(self)
        self.terminal = sys.stdout

    def write(self, line):
        self.terminal.write(line)
        if line != "\n":
            self.lines.append(line)

    def flush(self):
        self.terminal.flush()
