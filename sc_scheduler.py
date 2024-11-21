import datetime as dt
import os
from scheduler import Scheduler


import time
import subprocess
subprocess.Popen(r"C:\Users\Administrator\Downloads\rclone-v1.68.0-windows-amd64\rclone-v1.68.0-windows-amd64\gdrive.bat")
time.sleep(60)
hour_timeout=5

def run_long_function():
    try:
        subprocess.run(r"C:\Users\Administrator\Documents\i-have-never-used-it-aws\full_run.bat",timeout=hour_timeout*60*60)
        

    except Exception as e:
        print(e)
        print('-------------------------------------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------------------------')
    time.sleep(7200)
    try:

        subprocess.run(r"C:\Users\Administrator\Documents\aibot\linkedin_scrap.bat",timeout=hour_timeout*60*60)
    except Exception as e:
        print(e)
        print('-------------------------------------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------------------------')
    time.sleep(7200)
    try:

        subprocess.run(r"C:\Users\Administrator\Documents\throw\linkedin_send.bat",timeout=hour_timeout*60*60)
    except Exception as e:
        print(e)
        print('-------------------------------------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------------------------')

    time.sleep(7200)




schedule = Scheduler()
schedule.cyclic(dt.timedelta(days=1), run_long_function) 
print(schedule)

subprocess.run('minimize.cmd')
run_long_function()
while True:
    schedule.exec_jobs()
    time.sleep(1)