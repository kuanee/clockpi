import RPi.GPIO as GPIO
import time

# For this particular PIR, pin is pulled low if motion is detected. 
# Output pin requires PULL_UP
def getmovement(pin, time=False):
    """Get status of GPIO pin with motion sensor without interrupt checking
 
    Keyword Arguments:
    pin -- BCM pin number of PIR output
    time -- True to report time of logging
            False(default) to return only state of PIR sensor
    
    Returns: (bool, time(optional))
    Pins need to be cleaned using GPIO.cleanup()
    """

    # Set BCM Numbering for GPIO Pins
    GPIO.setmode(GPIO.BCM)
    # Set GPIO to input mode
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Current state of GPIO pin
    currentstate = GPIO.input(pin)
    # Return sensor state if time=true
    if time=True:
        return (currentstate,time.localtime())
    else:
        return (currentstate)

        
        






