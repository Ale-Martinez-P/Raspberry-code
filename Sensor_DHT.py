import Adafruit_DHT
# import time

SENSOR_DHT = Adafruit_DHT.DHT22
PIN_DHT = 2

def leerSensor():
    humedad, temperatura = Adafruit_DHT.read_retry(SENSOR_DHT, PIN_DHT)
    if humedad is not None and temperatura is not None:
        print("Temp:{0:0.1f}°C Hum:{1:0.1f}%", format(temperatura, humedad))
    else:
        print("Error en lectura")

leerSensor()