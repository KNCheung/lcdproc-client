#!/usr/bin/python

import subprocess
import psutil
import re
import uuid
from datetime import datetime
now = datetime.now
from time import sleep

from ScreenBase import ScreenBase

class Boinc(ScreenBase):
    def getCPUTemp(self):
        temp_raw = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf8")
        temp = re.findall(r"[\d\.]+", temp_raw)[0]
        return int(round(float(temp)))

    def getCPU(self):
        ret = psutil.cpu_percent()
        if ret >= 99.4:
            ret = '--%'
        else:
            ret = '{0:02d}%'.format(int(ret))
        return ret

    def run(self):
        title = self.screen.add_string_widget(uuid.uuid1(), "= BOINC =", 1, 1)
        text = self.screen.add_string_widget(uuid.uuid1(), "----", 1, 2)
        cpu = self.screen.add_string_widget(uuid.uuid1(), "--% --", 11, 2)
        time = self.screen.add_string_widget(uuid.uuid1(), "--:--", 11, 1)
        second = self.screen.add_vbar_widget(uuid.uuid1(), x=16, y=1, length=0)

        while True:
            status = subprocess.check_output("/usr/bin/boinccmd --get_simple_gui_info | /bin/grep 'fraction done' | /usr/bin/cut -d ':' -f2", shell=True).decode("utf8").split('\n')
            for i in range(len(status)):
                try:
                    x = float(status[i]) * 100.0
                    s = '{0}:{1:0.2f}% '.format(i, x)
                except:
                    s = 'NO TASK'
                text.set_text(s)
                cpu.set_text(self.getCPU() + ' ' + str(self.getCPUTemp()) + 'C')
                time.set_text(now().strftime("%H:%M"))
                second.set_length(now().second >> 3)
                sleep(1)

