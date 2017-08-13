import RPi.GPIO as GPIO
import time
import math

# pin defs
pwmPin = 18
ledPin = 23
butPin = 17

duty = 0

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm = GPIO.PWM(pwmPin, 200)
GPIO.output(ledPin, GPIO.LOW)
pwm.start(duty)

def mapFunc(x, inLo, inHi, outLo, outHi):
    inRange = inHi - inLo
    outRange = outHi - outLo
    inScale = (x - inLo) / inRange
    return outLo + (inScale * outRange)

x = 0

try:
    while 1:
        if GPIO.input(butPin): # not pressed
            step = 0.01
            GPIO.output(ledPin, GPIO.LOW)
        else:
            step = 0.04
            GPIO.output(ledPin, GPIO.HIGH)
            
        duty = mapFunc(math.sin(x),-1,1,0,100)
        x += step
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.01)
            
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()