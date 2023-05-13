import os

os.environ['KIVY_METRICS_DENSITY'] = '3'

import kivy
kivy.require('2.1.0')

from kivy.app import App
# from kivy.lang import Builder
# from kivy.core.window import Window

# class MainScreen:


class DemoApp(App):
    pass


if __name__ == '__main__':
    DemoApp().run()
