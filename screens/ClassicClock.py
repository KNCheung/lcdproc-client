#!/usr/bin/python 

from ScreenBase import ScreenBase
from datetime import datetime
now = datetime.now
from time import sleep

class ClassicClock(ScreenBase):
    def run(self):
        self.screen.set_heartbeat("off")

        date = self.screen.add_string_widget("date", "date", 5, 1)
        time = self.screen.add_string_widget("time", "time", 5, 2)

        while True:
            date.set_text(now().strftime("%X"))
            time.set_text(now().strftime("%x"))
            sleep(1)
