import Adafruit_DHT
import time

while True:
    sensor = Adafruit_DHT.DHT22
    pin = 4 #Cambiar segun el puerto que queremos usar
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    print ( 'Temperatura: ', temperatura)
    print ('Humedad: ', humedad)

time.sleep(1)