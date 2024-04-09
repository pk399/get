import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)

DAC = [8, 11, 7, 1, 0, 5, 12, 6]
LEDS = [2, 3, 4, 17, 27, 22, 10, 9]
COMP = 14
TROYKA = 13

GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LEDS, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(COMP, GPIO.IN)
GPIO.setup(TROYKA, GPIO.OUT, initial = GPIO.HIGH)


def bin2dec(n):
    return int(''.join([str(x) for x in n]), base = 2)

def dec2bin(n):
    assert(type(n) == int)
    assert(0 <= n and n < 256)
    return [int(d) for d in bin(n)[2:].zfill(8)]


def adc():
    for i in range(256):
        GPIO.output(DAC, dec2bin(i))
        time.sleep(0.003)
        if (GPIO.input(COMP)):
            return i
    return 255 # fix

try:
        while 1:
            n = adc()
            frac = n/255
            GPIO.output(LEDS, [0] * math.floor(8 * (1 - frac)) + [1] * math.ceil(8 * frac))
            time.sleep(0.04)
            
finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.output(LEDS, GPIO.LOW)
    GPIO.output(TROYKA, GPIO.LOW)
    GPIO.cleanup()


