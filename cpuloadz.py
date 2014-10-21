from piglow import PiGlow
import psutil
import os
import sys

piglow = PiGlow()
pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"

if os.path.isfile(pidfile): # a PID exists. Lets kill it and then run
    pidread = open('/tmp/mydaemon.pid', 'r')
    pidtokill = pidread.readline()
    cmdstring = "sudo kill %s" % (pidtokill) #this is the shell command string to kill the process
    os.system(cmdstring) # and this kills it with the predetermined command
    file(pidfile, 'w').write(pid)

else: #no pid file exists, lets go ahead and run
    file(pidfile, 'w').write(pid)

while 1:

    cpu = psutil.cpu_percent(interval=0.5)
    piglow.all(0)

    if cpu <= 10:
        piglow.green(1)
    elif cpu >= 11 and cpu <= 20:
        piglow.green(2)
    elif cpu >= 21 and cpu <= 30:
        piglow.green(3)
    elif cpu >= 31 and cpu <= 40:
        piglow.green(4)
    elif cpu >= 41 and cpu <= 50:
        piglow.yellow(5)
    elif cpu >= 51 and cpu <= 60:
        piglow.yellow(6)
    elif cpu >= 61 and cpu <= 70:
        piglow.yellow(7)
    elif cpu >= 71 and cpu <= 80:
        piglow.yellow(8)
    elif cpu >= 81 and cpu <= 90:
        piglow.red(9)
    elif cpu >= 91:
        piglow.red(10)
    else:
        piglow.green(1)