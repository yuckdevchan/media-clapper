import os
import sys
import subprocess
sys.path.append(os.path.abspath('.'))

from piclap import *

class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        Settings.__init__(self)
        self.method.value = 10000

    def on1Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

    def on2Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

    def on3Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

    def on4Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

    def on5Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

    def on6Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

    def on7Claps(self):
        subprocess.run("playerctl play-pause", shell=True)

def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
