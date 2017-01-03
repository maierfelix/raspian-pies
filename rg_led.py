import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_ROT = 22
LED_GRUEN = 23

GPIO.setup(LED_ROT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_GRUEN, GPIO.OUT, initial=GPIO.LOW)
return
print "Erfolg bis jetzt.."

GPIO.output(LED_ROT, GPIO.LOW)
GPIO.output(LED_GRUEN, GPIO.LOW)

try:

  while True:
    print "LED ROT 3s an"
    #GPIO.output(LED_ROT, GPIO.HIGH)
    GPIO.output(LED_GRUEN, GPIO.LOW)
    time.sleep(3)
    print "LED GRUEN 3s an"
    #GPIO.output(LED_ROT, GPIO.LOW)
    GPIO.output(LED_GRUEN, GPIO.HIGH)
    time.sleep(3)

except KeyboardInterrupt:
  GPIO.cleanup()
