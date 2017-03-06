#!/usr/bin/python

import socket

# 255.255.255.255 is the broadcast address of the network
#(equivalent to 0.0.0.0(IP Address) or FF:FF:FF:FF:FF:FF(MAC Address) )
# By using 255.255.255.255, every host on your network will be able to
# "intercept" the message. You may want to change it to suit your network.
# E.g. : 192.168.1.255 for 192.168.0/24
#        192.168.255.255 for 192.168.0.0/16
UDP_IP = "255.255.255.255"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Params: UDP_Port and sent_data
#
# UDP_Port specifies which port the program will bind to between the range of
# 0-65535.
#
# sent_data specifies the data you would like to broadcast to the network.


def SendUdp( UDP_PORT, sent_data ):

   sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
   sock.sendto(sent_data, (UDP_IP, UDP_PORT))

def RecvUdp( UDP_PORT ):

   sock.bind((UDP_IP, UDP_PORT))
   recv_data , addr = sock.recvfrom(1024)
   return recv_data


