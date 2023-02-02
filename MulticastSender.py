#Read CAN Interface and send to UDP Multicast address
import time
import can
from can.interfaces.udp_multicast import UdpMulticastBus

with UdpMulticastBus(channel=UdpMulticastBus.DEFAULT_GROUP_IPv6) as udpbus, \
                     can.ThreadSafeBus(interface='socketcan', channel='vcan0') as hwrbus:
    buffer = can.BufferedReader()
    can.Notifier(hwrbus, [buffer])
    try:
        while True:
            udpbus.send(buffer.get_message())
    except KeyboardInterrupt:
        buffer.stop()
        print('Stopping...')
        pass