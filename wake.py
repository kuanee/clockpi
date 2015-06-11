import time
import os
import datetime
import RPi.GPIO as GPIO
from pygame import mixer

# pin number and bounctime
pin = 14
btime = 5000


# List to keep track of movetimes
movetime = []

def addtolist(x, list):
    '''Takes a time_struct x and stores it in a datetime object, appending to a list list'''
    dtobject = datetime.datetime(x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_minute, x.tm_second)
    list.append(dtobject)
    return 

def tmindt()
    '''Convert time struct to datetime format (return)'''
    dtobject = datetime.datetime(x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_minute, x.tm_second)
    return dtobject

def alarmdatetime(string,date=None):
    '''Return alarm time of format HHMM as a datetime object
    Resolves to the earliest occurence of specified time unless date is specified'''
    dtobject = datetime.datetime()
    dtobject.hour = int(string[:2])
    dtobject.minute = int(string[2:])
    # Assume same year and month
    dtobject.year = time.localtime().tm_year
    dtobject.month = time.localtime().tm_mon
    # If date is specified, use it
    if(date):
        dtobject.day = date
        return dtobject
    # If specified time has passed, set next day, else, set today
    dtobject.day = time.localtime().tm_mday
    (x, y) = dtobject - addtolist(time.localtime())
    if (x < 0):
        dtobject.day = dtobject.day + 1
        return dtobject
    else:
        return dtobject

def occurences(window, list,time):
    '''Find occurences of times within window seconds of 'time' in the list'''
    pass

if(___name__ = '__main__'):
    
    os.chdir(alarmpath)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=addtolist(time.localtime(), movetime), bouncetime=btime)
        while True:
            if(occurences(300, movetime,datetime) > 5)
            #RINGALARM TODO
       
    except(KeyboardInterrupt):
        GPIO.cleanup()


