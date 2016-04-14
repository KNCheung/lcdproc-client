#!/usr/bin/python

from ScreenBase import ScreenBase
from time import sleep
from datetime import datetime
now = datetime.now
import psutil

class LargeClock(ScreenBase):
    def run(self): 
        h1 = self.screen.add_number_widget("h1", x=1, value=0)
        h2 = self.screen.add_number_widget("h2", x=4, value=0)
        m1 = self.screen.add_number_widget("m1", x=8, value=0)
        m2 = self.screen.add_number_widget("m2", x=11, value=0)
        sec = self.screen.add_string_widget("sec", '--', x=15, y=2)
        dot1 = self.screen.add_string_widget("d1", ".", x=7, y=1)
        dot2 = self.screen.add_string_widget("d2", ".", x=7, y=2)
        while True:
            t = now()
            h1.set_value(t.hour / 10)
            h2.set_value(t.hour % 10)
            m1.set_value(t.minute / 10)
            m2.set_value(t.minute % 10)
            sec.set_text('{0:02d}'.format(t.second))
            sleep(1)
