import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
while True:
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#4 means pin number 7 in raspberry pi
print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
temp_int = int(temperature)
if temp_int<20:
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
elif temp_int>20 and temp_int < 30:
GPIO.output(10,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
elif temp_int >= 30:
GPIO.output(12,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
