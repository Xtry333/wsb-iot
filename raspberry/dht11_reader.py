#!/usr/bin/python3
import sys
import time
import json
import Adafruit_DHT
from db import collection
from datetime import datetime

thetime = datetime.now()

DHT_PIN = 4  # GPIO PIN
DHT_SENSOR = Adafruit_DHT.AM2302  # sensor type
LOOP_DELAY = 30  # seconds
FILE_LOCATION = 'data/air-data.json' # air data file

print('AM2302 Reader started on ' + str(thetime) + ' on pin ' + str(DHT_PIN))

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor=DHT_SENSOR, pin=DHT_PIN)
        #print('Date: ' + str(datetime.now()) +
        #      ' Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        info = {"date": str(datetime.now()), "humidity": humidity, "temperature": temperature, "sensor": DHT_SENSOR}
        try:
            airDataFile = open(FILE_LOCATION, "r")
            air = json.load(airDataFile)
            info['air'] = air
        except (json.decoder.JSONDecodeError):
            print("json error")
        print(info)
        collection.insert_one(info)
        time.sleep(LOOP_DELAY)

except (KeyboardInterrupt):
    print('Goodbye.')
