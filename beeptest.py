import getmove
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        if (getmove.getmovement(14)):
            print('\a')
        time.sleep(1)
except(KeyboardInterrupt):
    GPIO.cleanup()
