import os

from steamworks import STEAMWORKS

# Declare the steamworks variable and create a new instance of the Steamworks class
steamworks = STEAMWORKS()

# Initialize Steam
steamworks.initialize()
my_steam64 = steamworks.Users.GetSteamID()
my_steam_level = steamworks.Users.GetPlayerSteamLevel()

print(f'Logged on as {my_steam64}, level: {my_steam_level}')

os.environ['KIVY_METRICS_DENSITY'] = '2.5'

import kivymd

from kivymd.app import MDApp

class DemoApp(MDApp):
    pass


if __name__ == '__main__':
    DemoApp().run()

