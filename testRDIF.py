from time import sleep
import paho.mqtt.client as mqtt
import sys
from Jetson_MFRC522 import SimpleMFRC522
import Jetson.GPIO as GPIO # GPIO library

# Pin Definition
red_led = 7
green_led = 11
# Set up the GPIO channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(red_led, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(green_led, GPIO.OUT, initial=GPIO.LOW) 

def on_message(client, userdata, message):#esta funcion se ejecuta cuando llega un mensaje
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    if str(message.payload.decode("utf-8"))=="ok":
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)
        sleep(5)
        GPIO.output(red_led, GPIO.HIGH)
        GPIO.output(green_led, GPIO.LOW)

reader = SimpleMFRC522()

try:
    client =mqtt.Client("Jetson-LectorRFID")
    client.on_message = on_message
    client.connect("localhost",1885)
    client.subscribe("Detection/masks")
    client.loop_start() #inicializa el loop que esta a la espera de mensajes
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        client.publish("Detection/RFID","TARJETAA")
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    client.loop_stop()
    raise
