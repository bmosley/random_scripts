#!/usr/bin/python

# Basic Sound Sensor Sample for Apple Pi project.
# bryanmosley@apple.com

import RPi.GPIO as GPIO
import time

# set up the GPIO
pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def sensor(pin):
    if GPIO.input(pin):
        print "sound high"
    else:
        print "sound low"

# this tells us if the pin goes HIGH or LOW
# matt - in this case we dont care if its HIGH or LOW we just want to detect anything.
GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)

# put a function on the pin and change when run.
GPIO.add_event_callback(pin, sensor)

# loop
while True:
    time.sleep(1)
