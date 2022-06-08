import RPi.GPIO as GPIO
import time

SENSOR = 7

def inicializarSensor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SENSOR, GPIO.IN)

def leerSensor(SENSOR):
    valor = GPIO.input(SENSOR)
    if (valor == 1):
        print('El suelo esta un poco Seco')
    else:
        print('El suelo esta Humedo')
    # return valor

def cerrarSensor():
    GPIO.cleanup(SENSOR)

inicializarSensor()
leerSensor(SENSOR)
GPIO.add_event_detect(SENSOR, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(SENSOR, leerSensor)
while True:
    time.sleep(0.1)