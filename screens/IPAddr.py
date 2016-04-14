#!/usr/bin/python

from ScreenBase import ScreenBase

class IPAddr(ScreenBase):
    def run(self):
        self.screen.set_heartbeat("off")

        while True:
            sleep(60)

