#!/usr/bin/env python2.5

import sys
import os
from socket import *

import util

port = 10000

(p, c) = socket.socketpair()


pid = os.fork()
if pid == 0 : # Child
    c.close()
    settings = p.recv(1024)
    hosts = util.set2hosts(settings)
    ss = socket.socket(AF_INET, SOCK_DGRAM, 0)
    results = {}
    for host in hosts :
        t0 = time()
        request = 'REQ %s %s' % (util.hostname(), host)
        peeraddr = (host, port)
        ss.sendto(request, peeraddr)
        result = p.recv()
        t1 = time()
        results[host] = (t1 - t0)
    for (to, time) in results.iteritems() :
        sys.stdout.write("%s %s %d" % (util.hostname(), to, time))
    os._exit(0)
else : # Parent
    p.close()
    us = socket(AF_INET, SOCK_DGRAM, 0)
    us.bind(("localhost", int(sys.argv[1])))
    sys.stdout.write('STANDBY %s' % util.hostname())
    settings = sys.stdin.read() # うまくやる
    c.sendall(settings)
    ss = socket.socket(AF_INET, SOCK_DGRAM, 0)
    while True :
        s = us.recvfrom(1024)
        prefix = s[0:3]
        suffix = s[3:]
        if prefix == 'REQ' :
            reply = 'REP' + suffix
            (peeraddr, peerport) = us.getpeername()
            ss.sendto(reply, (peeraddr, port))
        elif prefix == 'REP' :
            c.sendall(suffix)
