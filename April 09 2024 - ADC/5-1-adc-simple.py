import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

DAC = [8, 11, 7, 1, 0, 5, 12, 6]
COMP = 14
TROYKA = 13

GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(COMP, GPIO.IN)
GPIO.setup(TROYKA, GPIO.OUT, initial = GPIO.HIGH)


def dec2bin(n):
    assert(type(n) == int)
    assert(0 <= n and n < 256)
    return [int(d) for d in bin(n)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(DAC, dec2bin(i))
        time.sleep(0.001)
        if (GPIO.input(COMP)):
            return i
    return 256

try:
        while 1:
            input('Enter...')
            n = adc()
            v = (n/256)*3.3
            print(f'{v}V')
finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.output(TROYKA, GPIO.LOW)
    GPIO.cleanup()
