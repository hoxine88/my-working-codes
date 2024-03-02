import schedule
import time
import datetime


def MINUTE():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print(str(TNOW) + ' this print every minute')
    
def SECOND():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print(str(TNOW) + ' this print every 5 second')    
    
schedule.every(1).minutes.do(MINUTE)
schedule.every().minute.at(":05").do(SECOND)
schedule.every().minute.at(":10").do(SECOND)
schedule.every().minute.at(":15").do(SECOND)
while True:
    schedule.run_pending()
    time.sleep(1)