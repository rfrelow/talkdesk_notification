import subprocess
import os
import time

time_triggered = "00:00"

while 1:
	with open("silo.mytalkdesk.com_2016-10-10_17-23-2.txt", 'rb+') as f:
		if (os.path.exists("/proc/21154")):
			f.seek(-3,2)
			a = f.read()
			
			f.seek(-16,2)
			b = f.read()

			print a
			first_letter = a[:1]
			print first_letter
			
			print b
			current_time = b


			if (first_letter == '0' and current_time != time_triggered):

				os.system("bash ./hipchat.sh \"" + "There are currently 0 engineers available in queue" + "\"")
				time.sleep(600)
				time_triggered = current_time
	time.sleep(5)
