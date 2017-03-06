#!/usr/bin/python

import RPi.GPIO as GPIO
import gpio_udp
from gpio_udp import RecvUdp

UdpData = gpio_udp.RecvUdp(5005)

if UdpData == "Turn off LED" :
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(18,GPIO.OUT)
  GPIO.output(18,GPIO.LOW)
