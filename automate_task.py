import schedule
import time

def do_something():
    print("Testing...")

schedule.every().day.at("08:55").do(do_something)
while True:
    schedule.run_pending()
    time.sleep(60)
