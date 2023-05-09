import os
import sys
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
        pass

def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
