import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ROT = 25
GRUEN = 8
BLAU = 7

AN = GPIO.HIGH
AUS = GPIO.LOW

SPEED = 0.0001

# initialiseren
def init():
  GPIO.setup(ROT, GPIO.OUT, initial=AUS)
  GPIO.setup(GRUEN, GPIO.OUT, initial=AUS)
  GPIO.setup(BLAU, GPIO.OUT, initial=AUS)
  print "Initialisiert!"

# aufraeumen
def clean():
  GPIO.cleanup()

# setzt alle leds auf aus
def reset():
  GPIO.output(ROT, AUS)
  GPIO.output(GRUEN, AUS)
  GPIO.output(BLAU, AUS)

# nummer entspricht pin
def aktiviere(nummer):
  reset()
  GPIO.output(nummer, AN)

# initialisieren
init()

#aktiviere(ROT)
aktiviere(BLAU)
#aktiviere(GRUEN)

INTY_ROT = GPIO.PWM(ROT, 100)
INTY_BLAU = GPIO.PWM(BLAU, 100)
INTY_GRUEN = GPIO.PWM(GRUEN, 100)

INTY_ROT.start(1)
INTY_BLAU.start(1)
INTY_GRUEN.start(1)

INTY_ROT.ChangeDutyCycle(0)
INTY_BLAU.ChangeDutyCycle(0)
INTY_GRUEN.ChangeDutyCycle(0)

def setzeFarben(r, g, b, t):
  time.sleep(t)

intensity = 0
try: 
    #aktiviere(GRUEN)
    #time.sleep(SPEED)
    #aktiviere(ROT)
    #time.sleep(SPEED)
    #aktiviere(BLAU)

    #GPIO.output(ROT, AN)
    #GPIO.output(GRUEN, AN)
    #GPIO.output(BLAU, AN)

    #intensity += 2
    #INTY_ROT.ChangeDutyCycle(intensity)
    #INTY_BLAU.ChangeDutyCycle(intensity)
    #INTY_GRUEN.ChangeDutyCycle(intensity)
    #time.sleep(0.1)
    #print intensity
    #if intensity > 99:
    #  clean()
    #  break


  r = 50
  g = 10
  b = 0

  dirR = 1
  dirG = 1
  dirB = 1

  while True:

        INTY_ROT.ChangeDutyCycle(r);
        INTY_GRUEN.ChangeDutyCycle(g);
        INTY_BLAU.ChangeDutyCycle(b);

        r = r + dirR;

        if r == 100:
          dirR = -1;
        if r == 0:
          dirR = 1;

        g = g + dirG;

        if g == 100:
          dirG = -1;
        if g == 0:
          dirG = 1;

        b = b + dirB;

        if b == 100:
          dirB = -1;
        if b == 0:
          dirB = 1;
        print(r, g, b)
        time.sleep(0.05)

except KeyboardInterrupt:
  clean()
