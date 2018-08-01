# External module imports
import RPi.GPIO as GPIO
import time
import sys

if len(sys.argv) != 3:
    print "incorrect number of args"
    exit()

# Pin Definitons:
pin  = int(sys.argv[1])
state = (GPIO.HIGH if sys.argv[2] == "on" else GPIO.LOW)

print "setting %d to %s" %(pin, sys.argv[2])
print pin
print state

# Pin Setup:
GPIO.setmode(GPIO.BOARD)

# Initial state for LEDs:
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, state)

# no cleanup, leave state for relay
