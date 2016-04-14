#!/usr/bin/python

import threading
import uuid
from time import sleep

class Notify(threading.Thread):
    def __init__(self, lcd, msg, duration=5):
        threading.Thread.__init__(self)
        self.lcd = lcd

        self.name = str(uuid.uuid1())
        self.screen = self.lcd.add_screen(self.name)
        self.screen.set_duration(duration)

        self.msg = msg
        self.duration = duration

    def run(self):
        self.screen.set_heartbeat("off")

        msg_splited = self.msg.split("\n")

        line1 = self.screen.add_string_widget(uuid.uuid1(), msg_splited[0], 1, 1) 
        line2 = self.screen.add_string_widget(uuid.uuid1(), msg_splited[1], 1, 2)

        self.screen.set_priority("alert")
        sleep(self.duration)

        self.lcd.del_screen(self.name)

