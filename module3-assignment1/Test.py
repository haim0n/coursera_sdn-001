#! /usr/bin/python

'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from CustomTopo import CustomTopo

def simpleTest():
     	"Create and test a simple network"
	linkopts_core = {'bw':1000, 'max_queue_size':1000}
	linkopts_access = {'bw':100, 'max_queue_size':100}
	linkopts_edge = {'bw':10, 'max_queue_size':10}
	topo = CustomTopo(linkopts1=linkopts_core,
			linkopts2=linkopts_access,
			linkopts3=linkopts_edge,
			fanout=2)
      	net = Mininet(topo=topo, link=TCLink)
      	net.start()
      	print "Dumping host connections"
      	dumpNodeConnections(net.hosts)
      	print "Dumping switch connections"
      	dumpNodeConnections(net.switches)
      	print "Testing network connectivity"
      	#net.pingAll()
      	net.stop()

if __name__ == '__main__':
# Tell mininet to print useful information
	setLogLevel('info')
	simpleTest()

