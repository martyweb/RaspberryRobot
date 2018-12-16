#!/usr/bin/python

#--------------------------------------------
#
#
#--------------------------------------------

from adafruit_motorkit import MotorKit
import time
#import atexit
import xbox
import sys

debug = 1

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

def turnOffController():
        # Close out when done
        joy.close()

kit = MotorKit()            #init motors
joy = xbox.Joystick()       #Initialize joystick

print("Press Back button to exit")
# Loop until back button is pressed
while not joy.Back():

    speedLeft=0
    speedRight=0
    speedLeft = round(joy.leftY(),2)
    speedRight = round(joy.rightY(),2)
    #print("speedLeft", speedLeft)
    #print("speedRight", speedRight)

    if debug :
        sys.stdout.write('\r')
        # the exact output you're looking for:
        message = ("Lx,Ly ",fmtFloat(joy.leftX()),fmtFloat(joy.leftY()),"Rx,Ry ",fmtFloat(joy.rightX()),fmtFloat(joy.rightY()),"Ltrg ",fmtFloat(joy.leftTrigger()),"Rtrg ",fmtFloat(joy.rightTrigger()),"Speed R,L ", speedLeft,speedRight)
        sys.stdout.write(str(message))
        sys.stdout.flush()

    if speedLeft == 0:
        kit.motor2.throttle = None
    else:
        kit.motor2.throttle = speedLeft
    
    if speedRight == 0:
        kit.motor3.throttle = None
    else:
        kit.motor3.throttle = speedRight

    #myMotor2.setSpeed(int(abs(speedRight)))
    time.sleep(0.01)
    
    #print chr(13),
    #print("", end="", flush=True)
    
print("")   
