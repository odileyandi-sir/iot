import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOAR
D) GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.LOW)
while True:
if(GPIO.input(11)):
GPIO.output(3,GPIO.HIGH)
print("Intruder Detected!!")
else:
GPIO.output(3,GPIO.LOW)
print("NO Intruder")
