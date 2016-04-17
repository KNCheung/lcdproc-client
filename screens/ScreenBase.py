#!/usr/bin/python

import threading
import uuid

class ScreenBase(threading.Thread):
    def __init__(self, lcd, configFile):
        threading.Thread.__init__(self)
        self.lcd = lcd
        self.configFile = configFile

        self.name = str(self.__class__.__name__).split('.')[-1]
        self.screen = self.lcd.add_screen(self.name)
        print('Load {0}'.format(self.name))

        self.screen.set_heartbeat(self.config('heartbeat', 'off'))
        self.screen.set_duration(self.intConfig('duration', 5))

    def config(self, option, default=None):
        print('Read [{0}] <{1}>'.format(self.name, option))
        try:
            return self.configFile.get(self.name, option)
        except:
            return default

    def intConfig(self, option, default=0):
        return int(self.config(option, default))

    def floatConfig(self, option, default=0.0):
        return float(self.config(option, default))

    def boolConfig(self, option, default=False):
        tmp = self.config(option, 'False')
        return tmp.lower() in ['1', 'true', 'on']

