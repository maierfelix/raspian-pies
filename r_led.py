import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

ON = GPIO.HIGH
OFF = GPIO.LOW
ROT = 5
GRUEN = 4

GPIO.setup(ROT, GPIO.OUT, initial=OFF)
GPIO.setup(GRUEN, GPIO.OUT, initial=OFF)
GPIO.output(ROT, ON)
time.sleep(2)
GPIO.output(ROT, OFF)
GPIO.output(GRUEN, ON)
