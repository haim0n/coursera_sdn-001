#! /bin/bash

#DEBUG="log.level --DEBUG"
DEBUG=
pox.py forwarding.l2_learning misc.firewall $DEBUG &
sudo mn --topo single,3 --controller remote --mac
