#!/usr/bin/env python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, OVSController
from mininet.link import Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class LinuxRouter( Node ):
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):
    def build( self, **_opts ):
        firstIP = '172.18.0.10/16'  
        secondIP = '172.19.0.10/16' 

        router = self.addNode( 'r0', cls=LinuxRouter, ip=firstIP )
        s1, s2 = [ self.addSwitch( s ) for s in ( 's1', 's2' ) ]

        self.addLink( s1, router, intfName2='r0-eth1', params2={ 'ip' : firstIP }, bw=200, delay='1ms', loss=5) 
        self.addLink( s2, router, intfName2='r0-eth2', params2={ 'ip' : secondIP }, bw=200, delay='1ms', loss=5)


def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo, waitConnected=True, controller=OVSController)  
    _intf = Intf("br-2c9e805feb57", node=net['s1']) # client's interface
    _intf = Intf("br-a38886ecfd14", node=net['s2']) # server's interface
    net.start()
    info( '*** Routing Table on Router:\n' )
    info( net[ 'r0' ].cmd( 'route' ) )
    CLI( net )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
