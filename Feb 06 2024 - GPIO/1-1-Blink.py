import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.OUT)

INT = 0.4

for _ in range(100):
	gpio.output(24, 1)
	time.sleep(INT)
	gpio.output(24, 0)
	time.sleep(INT)
