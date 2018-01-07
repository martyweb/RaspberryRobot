#!/usr/bin/python

#--------------------------------------------
#ganked this code from: https://www.raspberrypi.org/forums/viewtopic.php?t=196006
#
#
#--------------------------------------------

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import xbox

while (True):
    mh = Adafruit_MotorHAT(addr=0x60)
    mh2 = Adafruit_MotorHAT(addr=0x60)


    myMotor = mh.getMotor(3)#forward and backwoard motor
    myMotor2 = mh2.getMotor(4)#left and right motor 

    joy = xbox.Joystick()         #Initialize joystick
    forword   = joy.leftX() #X-axis of the left stick for forward
    if forword >10 :
        myMotor.run(Adafruit_MotorHAT.FORWARD)
        myMotor.setSpeed(255)
        print("forward")
        time.sleep(0.01)
        joy.close()                   #Cleanup before exit

    joy = xbox.Joystick() 
    back   = joy.leftX() #X-axis of the left stick for back
    if back < 0 :     
        myMotor.run(Adafruit_MotorHAT.BACKWARD)
        myMotor.setSpeed(200)
        print("back")
        time.sleep(0.01)
        joy.close()
        
    joy = xbox.Joystick() 
    right   = joy.leftY() #y-axis of the left stick for right  
    if right >10:
        myMotor.run(Adafruit_MotorHAT.FORWARD)
        myMotor.setSpeed(175)
        print("right")
        time.sleep(0.01)
        joy.close()                   #Cleanup before exit

    joy = xbox.Joystick() 
    left   = joy.leftY() #y-axis of the left stick for left 
    if left < 0 :     
        myMotor.run(Adafruit_MotorHAT.BACKWARD)
        myMotor.setSpeed(175)
        print("left")
        time.sleep(0.01)
        joy.close()
            

    joy = xbox.Joystick() 
    stop   = joy.A() 
    if stop == 1 :     
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        myMotor.setSpeed(0)
        print("stop")#stop  by A button
        time.sleep(0.01)
        joy.close()