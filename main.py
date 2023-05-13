import os

os.environ['KIVY_METRICS_DENSITY'] = '2.5'

import kivymd

from kivymd.app import MDApp

class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    DemoApp().run()

