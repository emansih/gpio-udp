# Copyright 2017 Daniel Quah

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



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
        

