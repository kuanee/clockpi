import RPi.GPIO as GPIO
import time


output = 14

# Set GPIO Mode to use BCM numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO to input mode
GPIO.setup(output, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous_state = False
current_state = False

while True:
	time.sleep(0.1)
	previous_state = current_state
	current_state =GPIO.input(output)
	if current_state != previous_state:
		if not(current_state):
			print("Pin state:{0}".format(current_state))
		else:
			print("Pin state:{0}".format(current_state))

GPIO.cleanup()

