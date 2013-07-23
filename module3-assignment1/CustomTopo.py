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
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel

class CustomTopo(Topo):
	"Simple Data Center Topology"

    	"linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    	"fanout - number of child switch per parent switch"
   	def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        	# Initialize topology and default options
        	Topo.__init__(self, **opts)
        	# Add your logic here ...
		
		sw_list_access = []
		sw_list_edge = []
		core_switch = self.addSwitch('c1')
		sw_id = 0
		for i in irange (1, fanout):
			sw_id = sw_id + 1
			access_switch = self.addSwitch('a%s' %sw_id)
			self.addLink(core_switch, access_switch, **linkopts1)
			sw_list_access.append(access_switch)
	
		sw_id = 0
		for sw in sw_list_access:
			for i in irange (1, fanout):
				sw_id = sw_id + 1
				edge_switch = self.addSwitch('e%s' %sw_id)
				self.addLink(edge_switch, sw, **linkopts2)
				sw_list_edge.append(edge_switch)

		h_id = 0
		for sw in sw_list_edge:
			for i in irange (1, fanout):
				h_id = h_id + 1
				host = self.addHost('h%s' %h_id)
				self.addLink(host, sw, **linkopts3) 
		
        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }

