import schedule
import time as tm
from datetime import time,timedelta,datetime

def task():
    print("take a break, life is short!")
schedule.every(5).seconds.do(task)
while True:
    schedule.run_pending()
    tm.sleep(1)


def workout():
    print("take a walk!")
schedule.every().wednessday.at("2").minute.at(":40").seconds.do(workout)
while True:
    schedule.run_pending()
    tm.sleep(1)



    
def test():
    print("take your HTML test!")
schedule.every(1).minute.do(test)
while True:
    schedule.run_pending()
    tm.sleep(1)



def job():
    print("take your HTML test!")
schedule.every().day.at("10:00").minute.do(job)
while True:
    schedule.run_pending()
    tm.sleep(1)
