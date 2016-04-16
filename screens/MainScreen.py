#!/usr/bin/python

from ScreenBase import ScreenBase
import subprocess
import re
import psutil
from datetime import datetime
now = datetime.now
from time import sleep

class MainScreen(ScreenBase):
    def getCPUTemp(self):
        temp_raw = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf8")
        temp = re.findall(r"[\d\.]+", temp_raw)[0]
        return int(round(float(temp)))

    def run(self):
        time = self.screen.add_string_widget("time", "time", 1, 1)
        status = self.screen.add_string_widget("status", "xxx", 1, 2)

        while True:
            time.set_text(now().strftime("%b %d %a %H:%M"))
            cpu = psutil.cpu_percent()
            if cpu >= 99.4:
                cpu = '--'
            else:
                cpu = "{0:02.0f}".format(cpu)
            status.set_text("    {0}% {1}C".format(cpu, self.getCPUTemp()))
            sleep(3) 

