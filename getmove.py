import RPi.GPIO as GPIO
import time

# For this particular PIR, pin is pulled low if motion is detected. 
# Output pin requires PULL_UP
def getmovement(pin, timestamp=False):

    """Get status of GPIO pin with motion sensor without interrupt checking
 
    Keyword Arguments:
    pin -- BCM pin number of PIR output
    time -- True to report time of logging
            False(default) to return only state of PIR sensor
    
    Returns: (bool, time(optional))
    Pins need to be cleaned using GPIO.cleanup()
    """
    # Current state of GPIO pin
    currentstate = GPIO.input(pin)
    # Return sensor state if time=true
    if timestamp==True:
        return (currentstate,time.localtime())
    else:
        return (currentstate)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    try:
        while True:
            input("Press enter to get sensor state and timestamp...")
            (state, timestamp) = getmovement(14, timestamp=True)
            if(state):
                print("No motion at {0.tm_hour}:{0.tm_min:02d}:{0.tm_sec:02d}".format(timestamp, state))
            else:
                print("Motion at {0.tm_hour}:{0.tm_min:02d}:{0.tm_sec:02d}".format(timestamp, state))
 
    except(KeyboardInterrupt):
        print("\nProgram Killed")
   
        
        






