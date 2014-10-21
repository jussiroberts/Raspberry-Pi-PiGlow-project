#!/usr/bin/python

from piglow import PiGlow
from time import sleep
from datetime import datetime
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Int value for brightness')
parser.add_argument('integer', nargs='?', type=int, default='10') # default brightness of LED if no argument is given Set value in range 1-255)

args = parser.parse_args()



piglow = PiGlow()


### You can customise these settings ###

show12hr = 1            # Show 12 or 24hr clock - 0= 24hr, 1= 12hr
ledbrightness = args.integer      # Set brightness of LED - 1-255 (recommend 10-20, put 0 and you won't see it!)
hourflash = 2           # Choose how to flash change of hour - 1= white leds, 2= all flash

armtop = "s"            # h= hour, m= minutes, s= seconds
armright = "m"
armbottom = "h"

### End of customising ###

pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"

if os.path.isfile(pidfile): #if a pid file exists, we need to kill it
    print "%s already exists" % pidfile
    pidread = open('/tmp/mydaemon.pid', 'r')
    pidtokill = pidread.readline()
    print "this is the ID of the process you want to kill:", pidtokill
    #os.unlink(pidfile)
    cmdstring = "sudo kill %s" % (pidtokill) #this is the command string to kill the process
    os.system(cmdstring) # and this kills it with the predetermined command
    file(pidfile, 'w').write(pid)
    print "We ifed and our new pid is:"
    print pid
    piglow.all(0)

    hourcount = 0
    hourcurrent = 0

    while True:
        time = datetime.now().time()
        hour,min,sec = str(time).split(":")
        sec,micro = str(sec).split(".")
    
        hour = int(hour)
        if show12hr == 1:
            if hour > 12:
                hour = hour - 12

        min = int(min)
        sec = int(sec)


        binhour = "%06d" % int(bin(hour)[2:])
        binmin = "%06d" % int(bin(min)[2:])
        binsec = "%06d" % int(bin(sec)[2:])

        # Check if current hour is different and set ready to flash hour
        if hourcurrent != hour:
            hourcount = hour
            hourcurrent = hour

    
        if armbottom == "h":
            arm3 = list(binhour)
        elif armbottom == "m":
            arm3 = list(binmin)
        else:
            arm3 = list(binsec)
        led13 = ledbrightness if arm3[5] == "1" else 0
        piglow.led(13,led13)
        led14 = ledbrightness if arm3[4] == "1" else 0
        piglow.led(14,led14)
        led15 = ledbrightness if arm3[3] == "1" else 0
        piglow.led(15,led15)
        led16 = ledbrightness if arm3[2] == "1" else 0
        piglow.led(16,led16)
        led17 = ledbrightness if arm3[1] == "1" else 0
        piglow.led(17,led17)
        led18 = ledbrightness if arm3[0] == "1" else 0
        piglow.led(18,led18)

        if armright == "h":
            arm2 = list(binhour)
        elif armright == "m":
            arm2 = list(binmin)
        else:
            arm2 = list(binsec)
        led07 = ledbrightness if arm2[5] == "1" else 0
        piglow.led(7,led07)
        led08 = ledbrightness if arm2[4] == "1" else 0
        piglow.led(8,led08)
        led09 = ledbrightness if arm2[3] == "1" else 0
        piglow.led(9,led09)
        led10 = ledbrightness if arm2[2] == "1" else 0
        piglow.led(10,led10)
        led11 = ledbrightness if arm2[1] == "1" else 0
        piglow.led(11,led11)
        led12 = ledbrightness if arm2[0] == "1" else 0
        piglow.led(12,led12)


        if armtop == "h":
            arm1 = list(binhour)
        elif armtop == "m":
            arm1 = list(binmin)
        else:
            arm1 = list(binsec)
        led01 = ledbrightness if arm1[5] == "1" else 0
        piglow.led(1,led01)
        led02 = ledbrightness if arm1[4] == "1" else 0
        piglow.led(2,led02)
        led03 = ledbrightness if arm1[3] == "1" else 0
        piglow.led(3,led03)
        led04 = ledbrightness if arm1[2] == "1" else 0
        piglow.led(4,led04)
        led05 = ledbrightness if arm1[1] == "1" else 0
        piglow.led(5,led05)
        led06 = ledbrightness if arm1[0] == "1" else 0
        piglow.led(6,led06)


        # Flash the white leds for the hour
        if hourcount != 0:
            sleep(0.5)
            if hourflash == 1:
                piglow.white(ledbrightness)
            if hourflash == 2:
                piglow.all(ledbrightness)
            sleep(0.5)
            hourcount = hourcount - 1
        else:
            sleep(0.1)

else:
    file(pidfile, 'w').write(pid)
    print "we elsed and this is the pid for this script:"
    print pid
	
    piglow.all(0)

    hourcount = 0
    hourcurrent = 0

    while True:
        time = datetime.now().time()
        hour,min,sec = str(time).split(":")
        sec,micro = str(sec).split(".")
    
        hour = int(hour)
        if show12hr == 1:
            if hour > 12:
                hour = hour - 12

        min = int(min)
        sec = int(sec)


        binhour = "%06d" % int(bin(hour)[2:])
        binmin = "%06d" % int(bin(min)[2:])
        binsec = "%06d" % int(bin(sec)[2:])

        # Check if current hour is different and set ready to flash hour
        if hourcurrent != hour:
            hourcount = hour
            hourcurrent = hour

    
        if armbottom == "h":
            arm3 = list(binhour)
        elif armbottom == "m":
            arm3 = list(binmin)
        else:
            arm3 = list(binsec)
        led13 = ledbrightness if arm3[5] == "1" else 0
        piglow.led(13,led13)
        led14 = ledbrightness if arm3[4] == "1" else 0
        piglow.led(14,led14)
        led15 = ledbrightness if arm3[3] == "1" else 0
        piglow.led(15,led15)
        led16 = ledbrightness if arm3[2] == "1" else 0
        piglow.led(16,led16)
        led17 = ledbrightness if arm3[1] == "1" else 0
        piglow.led(17,led17)
        led18 = ledbrightness if arm3[0] == "1" else 0
        piglow.led(18,led18)

        if armright == "h":
            arm2 = list(binhour)
        elif armright == "m":
            arm2 = list(binmin)
        else:
            arm2 = list(binsec)
        led07 = ledbrightness if arm2[5] == "1" else 0
        piglow.led(7,led07)
        led08 = ledbrightness if arm2[4] == "1" else 0
        piglow.led(8,led08)
        led09 = ledbrightness if arm2[3] == "1" else 0
        piglow.led(9,led09)
        led10 = ledbrightness if arm2[2] == "1" else 0
        piglow.led(10,led10)
        led11 = ledbrightness if arm2[1] == "1" else 0
        piglow.led(11,led11)
        led12 = ledbrightness if arm2[0] == "1" else 0
        piglow.led(12,led12)


        if armtop == "h":
            arm1 = list(binhour)
        elif armtop == "m":
            arm1 = list(binmin)
        else:
            arm1 = list(binsec)
        led01 = ledbrightness if arm1[5] == "1" else 0
        piglow.led(1,led01)
        led02 = ledbrightness if arm1[4] == "1" else 0
        piglow.led(2,led02)
        led03 = ledbrightness if arm1[3] == "1" else 0
        piglow.led(3,led03)
        led04 = ledbrightness if arm1[2] == "1" else 0
        piglow.led(4,led04)
        led05 = ledbrightness if arm1[1] == "1" else 0
        piglow.led(5,led05)
        led06 = ledbrightness if arm1[0] == "1" else 0
        piglow.led(6,led06)


        # Flash the white leds for the hour
        if hourcount != 0:
            sleep(0.5)
            if hourflash == 1:
                piglow.white(ledbrightness)
            if hourflash == 2:
                piglow.all(ledbrightness)
            sleep(0.5)
            hourcount = hourcount - 1
        else:
            sleep(0.1)
