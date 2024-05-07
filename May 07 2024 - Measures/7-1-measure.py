import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# Максимально и минимально возможные
# напряжения на данной плате
MAXV = 207
MINV = 168

# Задержка в ЦАП
DELAY = 0.008

DAC = [8, 11, 7, 1, 0, 5, 12, 6] # DAC pins
COMP = 14                        # Comparator out pin
TROYKA = 13                      # Troyka V pin

# Pin setup
GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(COMP, GPIO.IN)
GPIO.setup(TROYKA, GPIO.OUT, initial = GPIO.HIGH)


# ADC function
def bin2dec(n):
    return int(''.join([str(x) for x in n]), base = 2)

def adc():
    state = [0] * 8
    
    for i in range(8):
        state[i] = 1
        GPIO.output(DAC, state)
        time.sleep(DELAY)
        if GPIO.input(COMP):
            state[i] = 0
    return bin2dec(state)


# Main script
start_time = time.time()
measurments = []

try:
        while 1:
            n = adc()
            measurments.append(n)
            print(f'{n}')
            
            if n == MAXV and GPIO.input(TROYKA) == GPIO.HIGH:
                GPIO.output(TROYKA, GPIO.LOW)
            elif n == MINV and GPIO.input(TROYKA) == GPIO.LOW:
                GPIO.output(TROYKA, GPIO.HIGH)
                # End the program
                break
finally:
    end_time = time.time()
    
    with open('settings.txt', 'wt') as o:
        # Сначала - частота дискретизации
        # Затем - шаг квантования
        o.write(f'{(end_time - start_time)/len(measurments)}\n{3.3/2**8}')
    
    with open('measurments.txt', 'wt') as o:
        o.write('\n'.join([str(x) for x in measurments]))
    
    GPIO.output(DAC, GPIO.LOW)
    GPIO.output(TROYKA, GPIO.LOW)
    GPIO.cleanup()

