import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p.start(0)
try:
    while 1:
            dc = int(input('Duty cycle? '))
            p.ChangeDutyCycle(dc)
            print('Voltage should be {:.4f}V'.format((dc/100)*3.3))
finally:
    p.stop()
    GPIO.cleanup()