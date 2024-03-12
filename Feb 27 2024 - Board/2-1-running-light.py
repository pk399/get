import RPi.GPIO as gpio
import time

LEDS = [2, 3, 4, 17, 27, 22, 10 , 9]

gpio.setmode(gpio.BCM)

for led in LEDS:
    gpio.setup(led, gpio.OUT)

for _ in range(3):
    for i in range(len(LEDS) + 1):
        if i > 0:
            gpio.output(LEDS[i - 1], 0)
        
        if i < len(LEDS):
            gpio.output(LEDS[i], 1)
        
        time.sleep(0.2)

for led in LEDS:
    gpio.output(led, 0)

gpio.cleanup()