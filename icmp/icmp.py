#!/usr/bin/env python3
# -*- coding: ascii -*-

import sys
from scapy.all import sr1,IP,ICMP

p = sr1(IP(dst=sys.argv[1])/ICMP(), timeout = 10)

if p:
    p.show()
else:
    print('{} is down'.format(sys.argv[1]))
