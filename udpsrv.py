import sys
from socket import *

if len(sys.argv) < 3 :
    print "Usage : %s PORT" % (sys.argv[0])
    sys.exit(1)

us = socket(AF_INET, SOCK_DGRAM, 0)
us.bind(("localhost", int(sys.argv[1])))

recv_counter = 0
print us
while True:
    s = us.recvfrom(1024)
    recv_counter += 1
    print recv_counter, s, s
