import RPi.GPIO as GPIO
from time import sleep

BOMBA = 38

def inicializarBomba():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BOMBA, GPIO.OUT)

def prenderBomba():
    GPIO.output(BOMBA, True)

def apagarBomba():
    GPIO.output(BOMBA, False)

def cerrarBomba():
    GPIO.cleanup(BOMBA)

inicializarBomba()
prenderBomba()
sleep(2)
apagarBomba()
cerrarBomba()