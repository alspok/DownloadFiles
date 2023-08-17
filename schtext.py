import schedule
from datetime import datetime 
import time

def schtest():
    dt = datetime.now()
    print(dt)

schedule.every(10).minutes.do(schtest)
while True:
    schedule.run_pending()
    time.sleep(1)