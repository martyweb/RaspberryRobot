#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(3) #right
myMotor2 = mh.getMotor(2) #left

myMotor.run(Adafruit_MotorHAT.FORWARD)
myMotor2.run(Adafruit_MotorHAT.FORWARD)

print "running 3"
myMotor.setSpeed(100)
#time.sleep(3)

print "running 1"
myMotor2.setSpeed(100)
#time.sleep(3)

myMotor.setSpeed(0)
myMotor2.setSpeed(0)

myMotor.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(1.0)


def runOption(x):
        return{
                'a':1,
                'b':2,
        }[x]



while (True):

        print "1. Forward"

        print "4. Right"
        print "5. Exit"

        option = input("Enter option:")

        output = runOption(option)

        print "output:"

        print output
        #print "Forward! "
        #myMotor.run(Adafruit_MotorHAT.FORWARD)

        #print "\tSpeed up..."
        #for i in range(255):
                #myMotor.setSpeed(i)
                #time.sleep(0.01)

        #print "\tSlow down..."
        #for i in reversed(range(255)):
                #myMotor.setSpeed(i)
                #time.sleep(0.01)

        #print "Backward! "
        #myMotor.run(Adafruit_MotorHAT.BACKWARD)

        #print "\tSpeed up..."
        #for i in range(255):
                #myMotor.setSpeed(i)
                #time.sleep(0.01)

        #print "\tSlow down..."
        #for i in reversed(range(255)):
                #myMotor.setSpeed(i)
                #time.sleep(0.01)

        #print "Release"
        #myMotor.run(Adafruit_MotorHAT.RELEASE)
        #time.sleep(1.0)
