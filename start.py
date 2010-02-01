#!/usr/bin/env python2.5

import sys
import os
import subprocess
import signal

def launch_gxpc(path='/usr/bin/gxpc') :
    """
    
    Arguments:
    - `path`:
    """
    cmd = (path, 'e', 'hostname')
    sp = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sp.stdin.write('START')
    out = sp.stdout.read()
    sp.stdin.write('CLI START')
    sp.stdin.write(setting)
    result = sp.stdout.read()
    f = open('result', 'w')
    f.write(result)
    os.kill(sp.pid, signal.SIGINT)

if __name__ == '__main__' :
    launch_gxpc(path='/home/kabe/local/bin/gxpc')

