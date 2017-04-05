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

# Send temperature data from DHT22 to network

import sys
import Adafruit_DHT
from gpio_udp import SendUdp

humidity, temperature = Adafruit_DHT.read_retry(22, 14)

if humidity is not None and temperature is not None:
   string_temp = str(round(temperature,2))
   SendUdp(5005,string_temp)
else:
    print 'Failed to get reading. Try again!'

