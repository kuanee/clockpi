import os
import RPi.GPIO as GPIO
import time


# GPIO input pin for sensor
pin = 14
# Time in between detections in miliseconds
btime = 5000
# Autosave time in seconds
save = 60
def writelog(pin):
    print("Motion detected on pin#{0}".format(pin))
    log.write('Motion detected at {0.tm_hour}:{0.tm_min:02d}:{0.tm_sec:02d}\n'.format(time.localtime()))
"""
# Create directory at home/pi if it does not exist
os.makedirs(os.path.expanduser('~/sleeplog'),exist_ok=True)
"""
# Make and Change Directory to sleeplog foder
os.makedirs('/home/pi/sleeplog', exist_ok=True)
os.chdir('/home/pi/sleeplog')

#Use new filenumber of form log# everytime
filenumber = 0
while (os.path.isfile("{0}.log".format(filenumber))):
    filenumber = filenumber + 1

# Set up GPIO input
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Write log whenever motion is detected
try:
    log = open('{0}.log'.format(filenumber), mode='a', encoding='utf-8')
    # Write date at top of file
    log.write('{0.tm_mday}\{0.tm_mon}\{0.tm_year}\n'.format(time.localtime()))
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=writelog, bouncetime=btime)
    while True:
# save every minute
        time.sleep(save)
        remove_event_detect(pin)
        log.close
        log = open('{0}.log'.format(filenumber), mode='a', encoding='utf-8')
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=writelog, bouncetime=btime)
        print("File saved and opened successfully")
except (KeyboardInterrupt):
    GPIO.cleanup()
    print("\nKeyboardInterrupt Detected.")
    print("All GPIOs cleaned up.")
    log.close
    print("Log succesfully saved as {0}".format(log.name))
    print("Succesfully exited")

except:
    GPIO.cleanup()
    print("All GPIOs cleaned up.")
    log.close
    print("Log succesfully saved as {0}".format(log.name))
    print("Succesfully exited")


