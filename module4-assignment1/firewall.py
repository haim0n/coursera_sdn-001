#! /usr/bin/python
'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 4 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''



log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''



class Firewall (EventMixin):
    _rule_prio = 0x7000

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")	

    def install_drop_all_rule (self, event):
        log.info("dropping all traffic !!")
        msg = of.ofp_flow_mod()
        msg.idle_timeout = 10000
        msg.hard_timeout = 10000
        msg.priority = self._rule_prio
        event.connection.send(msg)
    
    def install_firewall_rules (self):
        ''' TODO: parse file '''

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        self.install_drop_all_rule(event)
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
