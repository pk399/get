import RPi.GPIO as gpio

DAC = [8, 11, 7, 1, 0, 5, 12, 6][::-1]
numero = [0, 0, 0, 0, 0, 0, 0, 0]

gpio.setmode(gpio.BCM)

for led in DAC:
    gpio.setup(led, gpio.OUT)
    gpio.output(led, 0)

try:
    numero_dec = int(input('Enter the number you want (0-255): '))
    numero_dec = max(0, min(255, numero_dec))
except:
    numero_dec = 2**3 + 2**5

for i in range(0, len(numero)):
    numero[i] = numero_dec % 2
    numero_dec = numero_dec // 2
    
print(numero)
for i in range(0, len(DAC)):
    gpio.output(DAC[i], numero[i])

input('ENTER to quit...')
    
for led in DAC:
    gpio.output(led, 0)

gpio.cleanup()
