import datetime as dt
import os
from scheduler import Scheduler


import time
import subprocess

hour_timeout=5

def run_long_function():
    try:
        subprocess.run(r"C:\Users\Administrator\Documents\i-have-never-used-it-aws\full_run.bat",timeout=hour_timeout*60*60)
    except Exception as e:
        print(e)
        print('-------------------------------------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------------------------')



schedule = Scheduler()
schedule.cyclic(dt.timedelta(days=1), run_long_function) 
print(schedule)

# subprocess.run('minimize.cmd')
run_long_function()
while True:
    schedule.exec_jobs()
    time.sleep(1)