import RPi.GPIO as GPIO

SENSOR = 7

def inicializarSensor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SENSOR, GPIO.IN)

def leerSensor():
    valor = GPIO.input(SENSOR)
    if (valor == 1):
        #print('Seco',valor)
    else:
        #print('Humedo', valor)
    return valor

def cerrarSensor():
    GPIO.cleanup(SENSOR)

inicializarSensor()
valorSensor = leerSensor()
print(valorSensor)