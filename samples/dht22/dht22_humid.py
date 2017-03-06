#!/usr/bin/python

# Send humidity data from DHT22 to network

import sys
import Adafruit_DHT
from gpio_udp import SendUdp

humidity, temperature = Adafruit_DHT.read_retry(22, 14)

if humidity is not None and temperature is not None:
   string_humid = str(round(humidity,2))
   SendUdp(5005,string_humid)
else:
    print 'Failed to get reading. Try again!'

