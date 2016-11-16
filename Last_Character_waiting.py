import subprocess
import os
import time

last_waiting_time = "00:00"
current_waiting_time = "00:00"
triggered = 0

while 1:
	with open("silo.mytalkdesk.com_2016-11-7_18-5-24.txt", 'rb+') as f:
		if (os.path.exists("/proc/16361")):
			f.seek(-7,2)
			a = f.read()
			print a
			current_waiting_time = a[:5]
			print current_waiting_time
			
			if current_waiting_time != "00:00" and current_waiting_time != last_waiting_time:

				os.system("bash ./hipchat.sh \"" + "A call is currently waiting in the queue! " + current_waiting_time + "\"")
				last_waiting_time = current_waiting_time
				triggered = 1
				time.sleep(30)

			if current_waiting_time == "00:00" and triggered == 1:
				os.system("bash ./hipchat.sh \"" + "The call has been picked up! " + current_waiting_time + "\"")
				triggered = 0
				time.sleep(30)

	time.sleep(10)
