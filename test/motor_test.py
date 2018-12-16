#!/usr/bin/python

#--------------------------------------------
#ganked this code from: https://www.raspberrypi.org/forums/viewtopic.php?t=196006
#
#test
#--------------------------------------------

from adafruit_motorkit import MotorKit
kit = MotorKit()
import time

kit.motor2.throttle = 0.5
kit.motor3.throttle = 0.5
time.sleep(1)
kit.motor2.throttle = None
kit.motor3.throttle = None