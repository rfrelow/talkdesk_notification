import os
import time
from sys import argv
import smtplib
from email.mime.text import MIMEText


script, txt, calls_queued = argv

'''
author: __Dario__
'''

while 1:
        if (os.path.exists('/proc/')):
                calls_queued = open(calls_queued, 'rb+')
                calls_queued.seek(-7,2)
                calls_queued = calls_queued.read()
                calls_queued = calls_queued[:5]
                file = open(txt, 'rb+')
                file.seek(-7,2)
                file = file.read()
                wait_time =  file[:5]
                print wait_time
                if wait_time !="00:00":
                        call_number = 1
                        os.system("bash ./slack.sh \"" + "We have %s call(s) currently waiting in the queue! Time waiting is " + wait_time + "\"") % calls_queued
                        wait_time = current_wait_time
                        triggered = 1
                        time.sleep(30)

                if current_wait_time =="00:00" and triggered == 1:
                        os.system("bash ./slack.sh \"" + "The call has been picked up! " + current_wait_time + "\"")
                        triggered = 0
                        time.sleep(30)
        time.sleep(10)


'''
we can also do something like this to email Matney/Josh after a certain time:

fp = open(textfile, 'rb')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = 'Call in queue for over x amount of minutes'
msg['From'] = dingol@sciencelogic.com
msg['To'] = mmatney@sciencelogic.com
s = smtplib.SMTP('localhost')
s.sendmail(dingol@sciencelogic.com, [mmatney@sciencelogic.com], msg.as_string())
s.quit()
'''