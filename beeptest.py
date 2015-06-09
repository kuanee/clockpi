import getmove
import RPi.GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        if (getmovement(14)):
            print('\a')
        time.rest(1)
except(KeyboardInterrupt):
    GPIO.cleanup()
