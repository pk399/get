import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

DAC = [8, 11, 7, 1, 0, 5, 12, 6]
COMP = 14
TROYKA = 13

GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(COMP, GPIO.IN)
GPIO.setup(TROYKA, GPIO.OUT, initial = GPIO.HIGH)


def bin2dec(n):
    return int(''.join([str(x) for x in n]), base = 2)

def adc():
    state = [0] * 8
    
    for i in range(8):
        state[i] = 1
        GPIO.output(DAC, state)
        time.sleep(0.004)
        if GPIO.input(COMP):
            state[i] = 0
    return bin2dec(state)

try:
        while 1:
            #input('Enter...')
            n = adc()
            v = (n/256)*3.3
            print(f'{v}V')
finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.output(TROYKA, GPIO.LOW)
    GPIO.cleanup()

