#!/usr/bin/python

import threading
import uuid

class ScreenBase(threading.Thread):
    def __init__(self, lcd, duration=5, name=None):
        threading.Thread.__init__(self)
        self.lcd = lcd
        if name:
            self.name = name
        else:
            self.name = str(uuid.uuid1())
        self.screen = self.lcd.add_screen(self.name)
        self.screen.set_duration(duration)

