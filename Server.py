import socket
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
# next create a socket object
s = socket.socket()
print ("Socket successfully created")
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 8787
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))
# put the socket into listening mode
s.listen(5)
print ("socket is listening")
# a forever loop until we interrupt it or
# an error ocurs

while True:
# Establish connection with client.
c, addr = s.accept()
print ('Got connection from', addr )
# send a thank you message to the client. encoding to send byte type.
c.send('Thank you for connecting'.encode())
while True:
if GPIO.input(7):
c.send("1".encode())
print("Intruder Detected")
else:
c.send("0".encode())
print("No Intruder")
