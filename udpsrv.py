from socket import *

us = socket(AF_INET, SOCK_DGRAM, 0)
us.bind(("localhost", 3000))

recv_counter = 0
while True:
    s = us.recvfrom(1024)
    recv_counter += 1
    print recv_counter, s

