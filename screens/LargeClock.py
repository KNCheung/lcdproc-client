#!/usr/bin/python

from ScreenBase import ScreenBase
from time import sleep
from datetime import datetime
now = datetime.now
import psutil

import Adafruit_DHT as dht

from Timer import PeriodicTimer

class LargeClock(ScreenBase):
    dot = ' '
    def tickerWrapper(self, a, b):
        def f():
            a.set_text(self.dot)
            b.set_text(self.dot)
            if self.dot == ' ':
                self.dot = '.'
            else:
                self.dot = ' '
        return f

    def run(self): 
        pin = self.intConfig('sensorPort', 18)
        
        h1 = self.screen.add_number_widget("h1", x=1, value=0)
        h2 = self.screen.add_number_widget("h2", x=4, value=0)
        m1 = self.screen.add_number_widget("m1", x=8, value=0)
        m2 = self.screen.add_number_widget("m2", x=11, value=0)
        temp = self.screen.add_string_widget("temp", '--', x=15, y=1)
        humidity = self.screen.add_string_widget("humidity", '--', x=15, y=2)

        dot1 = self.screen.add_string_widget("d1", ".", x=7, y=1)
        dot2 = self.screen.add_string_widget("d2", ".", x=7, y=2)
        ticker = PeriodicTimer(self.floatConfig('tickerInterval', 0.5), self.tickerWrapper(dot1, dot2))
        ticker.start()

        while True:
            try:
                h, t = dht.read_retry(dht.AM2302, pin, retries=5, delay_seconds=2)
            except RuntimeError:
                h, t = (None, None)

            if h or t:
                temp.set_text("{0:02.0f}".format(t))
                humidity.set_text("{0:02.0f}".format(h))
            else:
                temp.set_text("--")
                humidity.set_text("--")

            for _ in range(12):
                t = now()
                h1.set_value(t.hour / 10)
                h2.set_value(t.hour % 10)
                m1.set_value(t.minute / 10)
                m2.set_value(t.minute % 10)
                sleep(5)
