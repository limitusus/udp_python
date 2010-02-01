import sys
from socket import *

if len(sys.argv) < 4 :
    print "Usage : %s HOST PORT MESSAGE" % (sys.argv[0])
    sys.exit(1)

us = socket(AF_INET, SOCK_DGRAM, 0)
us.sendto(sys.argv[3], (sys.argv[1], int(sys.argv[2])))
