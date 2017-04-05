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

import RPi.GPIO as GPIO
import gpio_udp
from gpio_udp import RecvUdp

UdpData = gpio_udp.RecvUdp(5005)

if UdpData == "Turn on LED" : 
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(18,GPIO.OUT)
  GPIO.output(18,GPIO.HIGH)

