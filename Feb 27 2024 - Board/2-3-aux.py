import RPi.GPIO as gpio
import time

LEDS = [2, 3, 4, 17, 27, 22, 10 , 9]
AUX = [21, 20, 26, 16, 19, 25, 23, 24]

gpio.setmode(gpio.BCM)

for led, aux in zip(LEDS, AUX):
    gpio.setup(led, gpio.OUT)
    gpio.output(led, 1)
    gpio.setup(aux, gpio.IN)

try:
    while 1:
        for led, aux in zip(LEDS, AUX):
            gpio.output(led, gpio.input(aux))
except KeyboardInterrupt:
    pass

for led in LEDS:
    gpio.output(led, 0)

gpio.cleanup()
