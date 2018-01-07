#!/usr/bin/python

#--------------------------------------------
#ganked this code from: https://www.raspberrypi.org/forums/viewtopic.php?t=196006
#
#test
#--------------------------------------------

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import xbox

debug = 1

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def turnOffController():
        # Close out when done
        joy.close()

atexit.register(turnOffMotors)
atexit.register(turnOffController)

mh = Adafruit_MotorHAT(addr=0x60)
mh2 = Adafruit_MotorHAT(addr=0x60)

myMotor2 = mh.getMotor(3)#right
myMotor = mh2.getMotor(2)#left motor 

joy = xbox.Joystick()         #Initialize joystick

startSpeed = 2

print("Xbox controller sample: Press Back button to exit")
# Loop until back button is pressed
while not joy.Back():

    speedLeft=0
    speedRight=0
    speedLeft = round(joy.leftY()*255,2)
    speedRight = round(joy.rightY()*255,2)

    if debug :
        # Left analog stick
        print "Lx,Ly ",fmtFloat(joy.leftX()),fmtFloat(joy.leftY()),
        # Right analog stick
        print "Rx,Ry ",fmtFloat(joy.rightX()),fmtFloat(joy.rightY()),

        # Right trigger
        print "Ltrg ",fmtFloat(joy.leftTrigger()),
        # Right trigger
        print "Rtrg ",fmtFloat(joy.rightTrigger()),

        print "Speed R,L ", speedLeft,speedRight,


    #if abs(speedLeft) > startSpeed :
    if speedLeft > 1 * startSpeed :
        myMotor.run(Adafruit_MotorHAT.FORWARD)
        print("forward left"),
    elif speedLeft < -1 * startSpeed :
        myMotor.run(Adafruit_MotorHAT.BACKWARD)
        print("back left"),
    else :
        speedLeft = 0

    myMotor.setSpeed(int(abs(speedLeft)))
    time.sleep(0.01)
    
    
    if speedRight > 1 * startSpeed :
        myMotor2.run(Adafruit_MotorHAT.FORWARD)
        print("forward right"),
    elif speedRight < -1 * startSpeed :
        myMotor2.run(Adafruit_MotorHAT.BACKWARD)
        print("back right"),
    else :
        speedLeft = 0

    myMotor2.setSpeed(int(abs(speedRight)))
    time.sleep(0.01)
    
    print chr(13),
    
print ""
