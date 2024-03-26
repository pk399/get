import RPi.GPIO as GPIO

DAC = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(DAC, GPIO.OUT, initial=GPIO.LOW)

def dec2bin(n):
    assert(type(n) == int)
    assert(0 <= n and n < 256)
    return [int(d) for d in bin(n)[2:].zfill(8)]

try:
    while 1:
        inp = input('Please enter a number (0-255): ')
        if (inp.startswith('q')):
            print('Quitting...')
            break
        
        try:
            n = int(inp)
            if (n < 0):
                print('Please enter a non-negative number')
                continue
            if (n > 255):
                print('Please enter a number below 256')
                continue
        except ValueError:
            try:
                float(inp)
                print('Please enter a whole number')
            except ValueError:
                print('Please enter a number')
            continue

        GPIO.output(DAC, dec2bin(n))
        print('Voltage should be {:.2f}V'.format((n/256)*3.3))
finally:
    GPIO.output(DAC, GPIO.LOW)
    GPIO.cleanup()
