from threading import Timer
from time import sleep
import threading
import datetime
import sys

def timer_func():
    print("I am rules")

timer = threading.Timer(4.0, timer_func)
timer.start()

while (True):
    sys.stdout.write('\r'+ str(datetime.datetime.now()))
    sleep(0.0001)