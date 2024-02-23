import schedule 
import time 
import subprocess
import datetime

def job():
    time_at_execution = datetime.datetime.now()
    print(f"Executing main.py at {time_at_execution}")
    subprocess.run(["python", "main.py"], check=True)

#Schedule the job every 10 minutes
schedule.every(10).minutes.do(job)

print("Scheduler started. Running main.py every 10 minutes")

job()
while True: 
    schedule.run_pending()
    time.sleep(1)