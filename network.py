//needs to be implemented

import psutil

while 1:

	cputiem = psutil.cpu_times()
	cpu = psutil.cpu_percent(interval=0.5)
	
	print cpu
	print cputiem
	
