#!/usr/bin/python

import uuid
from time import sleep

from ScreenBase import ScreenBase

class ListChars(ScreenBase):
    def run(self):
        coor = self.screen.add_string_widget(uuid.uuid1(), "0123456789", 4, 1)
        chars = map(lambda n: self.screen.add_string_widget(str(n), "-", 4 + n, 2), range(10))
        prefix = self.screen.add_string_widget(uuid.uuid1(), "00", 1, 2)

        while True:
            for i in range(25):
                prefix.set_text("{0:02d}".format(i))
                for j in range(10):
                    chars[j].set_text(chr(i*10+j))
                sleep(2)

