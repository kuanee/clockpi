import os
import RPi.GPIO
import time

# GPIO input pin for sensor
pin = 14
# Time in between detections
btime = 30000

def writelog(pin):
    print("Motion detected on pin#{0}".format(pin))
    log.write('Motion detected on {0.tm_hour}:{0.tm_min:02d}:{0.tm_sec:02d}'.format(time.localtime())

# Create directory at home/pi if it does not exist

os.makedirs(os.path.expanduser('~/sleeplogs'),exist_ok=True)

# Use new filenumber of form log# everytime
filenumber = 0
while not (isfile("{}.log".format(filenumber)))
    filenumber = filenumber + 1

# Set up GPIO input
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Write log whenever motion is detected
try:
    log = open('{0}.log'.format(filenumber), mode='w', encoding='utf-8')
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=writelog, bouncetime=btime)
    while True:
        pass
except (KeyboardInterrupt):
    GPIO.cleanup()
    print("\nKeyboardInterrupt Detected.")
    print("All GPIOs cleaned up.")
    log.close
    print("Log succesfully saved as {0}".format(log.name))
    print("Succesfully exited")


