#!/usr/bin/python

import threading
import time

class PeriodicTimer(threading.Thread):
    def __init__(self, interval, func):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.func = func
        self.interval = interval

    def run(self):
        end = time.time() + self.interval
        while True:
            try:
                time.sleep(end - time.time())
                self.func()
            except IOError as e:
                print("ERROR: maybe the period was too short.")
            end += self.interval

if __name__ == "__main__":
    def f():
        print('tick')
    t = LoopingTimer(1.0, f)
    t.start()
    while True:
        time.sleep(600000)
