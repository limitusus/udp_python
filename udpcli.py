from socket import *

us = socket(AF_INET, SOCK_DGRAM, 0)
for i in range(0,100) :
    us.sendto("hoge", ("localhost", 3000))
