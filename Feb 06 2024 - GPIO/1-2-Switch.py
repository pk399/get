import RPi.GPIO as gpio


gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.OUT)
gpio.setup(23, gpio.IN)

#while 1:
gpio.output(24, gpio.input(23))
