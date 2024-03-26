import RPi.GPIO as GPIO
import time

PERIOD = 1250 # milliseconds

DAC = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(DAC, GPIO.OUT, initial=GPIO.LOW)

def dec2bin(n):
    assert(type(n) == int)
    assert(0 <= n and n < 256)
    return [int(d) for d in bin(n)[2:].zfill(8)]

t = 0 # discrete time

try:
    while 1:
        t = (t + 1) % 512
        if t % 512 < 256:
            n = t % 256
        else:
            n = 255 - t % 256
            
        GPIO.output(DAC, dec2bin(n))
        
        time.sleep(PERIOD / (1000 * 512))
finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup()