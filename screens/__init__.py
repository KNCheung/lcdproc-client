#!/usr/bin/python


screens = {}

from Boinc import Boinc
screens['Boinc'] = Boinc

from MainScreen import MainScreen
screens['MainScreen'] = MainScreen

from ClassicClock import ClassicClock
screens['ClassicClock'] = ClassicClock

from IPAddr import IPAddr
screens['IPAddr'] = IPAddr

from Notify import Notify
screens['Notify'] = Notify

from Test import Test
screens['Test'] = Test

from LargeClock import LargeClock
screens['LargeClock'] = LargeClock

