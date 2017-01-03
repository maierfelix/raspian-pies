import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# gpio pins
MOTOR_A=[17,18,27,22]
MOTOR_B=[23,24,25,4]

# servo got 4 magnets sequences
MAG_1=[1,0,0,0]
MAG_2=[0,1,0,0]
MAG_3=[0,0,1,0]
MAG_4=[0,0,0,1]

def setup(motor):
  GPIO.setup(motor[0],0)
  GPIO.setup(motor[1],0)
  GPIO.setup(motor[2],0)
  GPIO.setup(motor[3],0)

def move(array,speed,duration,dir):
  motor = array
  if dir == 0: motor = list(reversed(array))
  idx = 0
  while idx < duration:
    idx += 1
    i = idx&2+1
    GPIO.output(motor[0], MAG_1[i])
    GPIO.output(motor[1], MAG_2[i])
    GPIO.output(motor[2], MAG_3[i])
    GPIO.output(motor[3], MAG_4[i])
    time.sleep(speed)

try:
  setup(MOTOR_A)
  setup(MOTOR_B)
  move(MOTOR_A, 0.3, 1000, 0)
  move(MOTOR_A, 0.003, 1000, 1)
  # move this into second thread?
  move(MOTOR_B, 0.003, 1000, 0)
  move(MOTOR_B, 0.003, 1000, 1)
  GPIO.cleanup()

except KeyboardInterrupt:
  GPIO.cleanup()
