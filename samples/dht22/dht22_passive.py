#!/usr/bin/python

# This is a passive DHT22 script and will *ONLY* act upon receiving a UDP "ping"
# It is achieved by utilizing both sending and receiving functions.

import sys
import Adafruit_DHT
import gpio_udp

humidity, temperature = Adafruit_DHT.read_retry(22, 14)
UdpPort = 5005

UdpData = gpio_udp.RecvUdp(UdpPort) 

# When the script receives "Please give me temperature data.", take temp reading and broadcast a 
# message, otherwise it will remain "sleeping".
if UdpData == "Please give me temperature data." :
    
    if humidity is not None and temperature is not None:
      string_temp = str(round(temperature,2))
      gpio_udp.SendUdp(UdpPort,string_temp)
    else:
      print 'Failed to get reading. Try again!'


elif UdpData == "Please give me humidity data." :
      
    if humidity is not None and temperature is not None:
         string_humid = str(round(humidity,2))
         gpio_udp.SendUdp(UdpPort,string_humid)
    else:
         print 'Failed to get reading. Try again!'
        

