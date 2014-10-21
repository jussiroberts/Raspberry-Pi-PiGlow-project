from piglow import PiGlow
import os
import sys

piglow = PiGlow()

pid = str(os.getpid())
#pidread = open('/tmp/mydaemon.pid', 'r')
pidfile = "/tmp/mydaemon.pid"


if os.path.isfile(pidfile): #if a pid file exists, we need to kill it
    pidread = open('/tmp/mydaemon.pid', 'r')
    pidtokill = pidread.readline()
    print "this is the ID of the process we killed:", pidtokill
    cmdstring = "sudo kill %s" % (pidtokill) #this is the command string to kill the process
    os.system(cmdstring) # and this kills it with the predetermined command
    os.unlink(pidfile)
    piglow.all(0)
    sys.exit()
else:
    file(pidfile, 'w').write(pid)
    print "we elsed and this is the pid for this script:"
    print pid
    os.unlink(pidfile)
    piglow.all(0)
    sys.exit()
