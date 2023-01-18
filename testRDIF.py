from time import sleep
import paho.mqtt.client as mqtt
import sys
from Jetson_MFRC522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        client =mqtt.Client("Jetson-LectorRFID")
        client.connect("localhost",1885)
        client.publish("Detection/RFID","TARJETAA")
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
